from collections import Counter
from itertools import chain

from cluster import Cluster
from create_dataset import results
from embedding import Embedding
from plot import Plot

data = list(chain(*results))
# data = results
enb = Embedding(data).create_embeddings()
# enb = Embedding(data).load()
clustering = Cluster(enb, eps=0.075, min_samples=15)
projection = clustering.create_projection()
cluster = clustering.create_clusters(projection)

plot = Plot(cluster, projection)
plot.create_plot()
# plot.save(f'images/{perplexity}.png')
plot.show()

print(Counter(cluster.labels_))
# print(cluster.labels_[:10])
# print(cluster.labels_[10:20])
# print(cluster.labels_[20:25])
# print(cluster.labels_[25:])
