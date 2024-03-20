from collections import defaultdict

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from sklearn.cluster import DBSCAN
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm
from sklearn.manifold import TSNE
# from tsnecuda import TSNE
import numpy as np
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///products.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

results = [
    "The fabric turned out to be very rough to the touch, which does not meet the expectations of a quality product.",
    "The quality of the fabric does not match the price. After several erasures, it lost its shape.",
    "The fabric looks very bad and does not withstand erasure. I do not recommend it.",
    "The quality of the fabric leaves much to be desired. After the first erasure, it lost its colors.",
    "The fabric is very rough and does not retain its shape. I do not recommend it for everyday wear.",
    "The quality of the fabric does not meet expectations. After several erasures, it lost its texture.",
    "The fabric looks very bad and does not withstand erasure. I do not recommend it for everyday wear.",
    "The quality of the fabric leaves much to be desired. After the first erasure, it lost its colors.",
    "The fabric is very rough and does not retain its shape. I do not recommend it for everyday wear.",
    "The quality of the fabric does not meet expectations. After several erasures, it lost its texture.",

    "The screen brightness exceeded my expectations. The video looks much brighter than on other devices.",
    "The screen brightness is excellent, which makes watching videos and games more enjoyable.",
    "The screen brightness stands out among other models. Visually, the device looks much brighter.",
    "The brightness of the screen exceeded my expectations. The video looks much brighter than on other devices.",
    "The screen brightness is excellent, which makes watching videos and games more enjoyable.",
    "The brightness of the screen stands out among other models. Visually, the device looks much brighter.",
    "The brightness of the screen exceeded my expectations. The video looks much brighter than on other devices.",
    "The screen brightness is excellent, which makes watching videos and games more enjoyable.",
    "The screen brightness stands out among other models. Visually, the device looks much brighter.",
    "The brightness of the screen exceeded my expectations. The video looks much brighter than on other devices.",
    'You have the butifully cat'
]


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    link = Column(String)
    orig_link = Column(String)
    votes = Column(Integer)
    year = Column(Integer)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == self.id


embed_model = HuggingFaceEmbedding('BAAI/bge-base-en-v1.5')

# query = session.query(Product.id, Product.description)
# results = query.all()

ar = []
for result in tqdm(results):
    s = embed_model.get_text_embedding(result)  # [1])
    a = np.array(s)
    ar.append(a)
ar = np.array(ar)


# np.save('data.np', ar)
# quit()

# ar = np.load('data.np.npy')[:100]


def create_cluster(index=0, n_components=2, perplexity=950, eps: float = 2, min_samples=2, learning_rate=100):
    tsne = TSNE(n_components=n_components, perplexity=perplexity, learning_rate=learning_rate)
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    data_array = tsne.fit_transform(ar)
    clustering = dbscan.fit(data_array)
    labels = clustering.labels_
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(set(labels)))]

    d = defaultdict(list)
    for result, label, data in zip(results, labels, data_array):
        d[label].append([result, data])

    for ind, (label, datas), color in zip(range(len(d)), d.items(), colors):
        result = datas[0][0]  # [0]
        data = []
        res = []
        for i in datas:
            data.append(i[1])
            res.append(i[0])
        data = np.array(data)
        plt.plot(data[:, 0], data[:, 1], "o", markerfacecolor=tuple(color), markeredgecolor="k", markersize=14,
                 label=str(ind + 1))
        print(ind + 1, '  \t', len(data), '  \t', result)  # [1])
        print('\t\t\t\t ', *res, sep='\n\t\t\t\t ')

    print('count:', len(d))
    plt.scatter(data_array[:, 0], data_array[:, 1], c=labels, cmap='viridis')
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.05))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'p={perplexity}  {eps=}  ms={min_samples}  lr={learning_rate}  cnt={len(d)}')
    # plt.savefig(f'data/{index:>05}.png')
    # plt.close()
    plt.show()
    # plt.imsave(f'data/{perplexity}/{eps}/{min_samples}/{len(d)}.png')


# def create_cluster(n_components=2, perplexity=950, eps: float = 2, min_samples=2):
#     tsne = TSNE(n_components=n_components, perplexity=perplexity, learning_rate=1000)
#     data_array = tsne.fit_transform(ar)
#
#     plt.scatter(data_array[:, 0], data_array[:, 1])
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title(f'{perplexity=}  {eps=}  {min_samples=}')
#     plt.show()
#     # plt.savefig(f'data/{perplexity:>03}.png')
#     # plt.close()

index = 0
# for perplexity in tqdm(range(1, 19, 1)):
#     for eps_ in tqdm(range(1, 200, 40)):
#         for min_samp in range(2, 9, 2):
#             for learning_rate in range(1, 10, 2):
#                 create_cluster(index=index, perplexity=perplexity, eps=eps_, min_samples=min_samp, learning_rate=learning_rate)
#                 index += 1
create_cluster(perplexity=10, eps=2500, min_samples=3, learning_rate=1000)
