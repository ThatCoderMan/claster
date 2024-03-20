# results = {
#     'cluster1': ['Ткань очень плохая, не выдерживает стирки.', 'Ткань очень плохая, но не очень плохая.', 'Ткань очень плохая, но не очень плохая.'],
#     'cluster2': ['Качество материалов низкое, не держится всю ночь.', 'Качество материалов низкое, но не очень низкое.', 'Качество материалов низкое, но не очень низкое.'],
#     'cluster3': ['Плохая батарея, не держится всю ночь.', 'Плохая батарея, но не очень плохая.', 'Плохая батарея, но не очень плохая.'],
#     'cluster4': ['Экран очень яркий и четкий.', 'Экран очень яркий, но не очень яркий.', 'Экран очень яркий, но не очень яркий.'],
#     'cluster5': ['Ткань очень плохая, но не очень плохая.', 'Качество материалов низкое, но не очень низкое.', 'Плохая батарея, но не очень плохая.']
# }
#


from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///products.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


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


query = session.query(Product.description)
results = query.all()[:1000]
