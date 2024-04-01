from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

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
results = query.all()


# results = [
#     "Insufficient fabric quality: Buying a jacket turned out to be a disappointment. The fabric was not as promised.",
#     "The fabric does not meet expectations: The jacket I bought does not meet my expectations. The fabric was not the same as in the photo.",
#     "Unsatisfactory fabric quality: The jacket I purchased did not meet my expectations. The fabric was not the same as on the website.",
#     "The fabric does not match the description: The purchase of the jacket was unsuccessful. The fabric was not the same as on the website.",
#     "Insufficient fabric quality: The jacket I bought does not meet my expectations. The fabric was not the same as in the photo.",
#     "The fabric does not meet expectations: Buying a jacket turned out to be a disappointment. The fabric was not as promised.",
#     "Unsatisfactory fabric quality: The jacket I purchased did not meet my expectations. The fabric was not the same as on the website.",
#     "The fabric does not match the description: The jacket I bought does not meet my expectations. The fabric was not the same as in the photo.",
#     "Insufficient fabric quality: The purchase of the jacket was unsuccessful. The fabric was not the same as on the website.",
#     "The fabric does not meet expectations: The jacket I purchased did not meet my expectations. The fabric was not as promised.",
#
#     "Unsatisfactory durability: The zipper breaks after a while, which is a big disappointment.",
#     "Premature failure: The jacket I bought turned out to be short-lived. Lightning breaks after a while.",
#     "Insufficient durability: The zipper on the jacket was not as strong as promised. It breaks down after a while.",
#     "Not meeting expectations: Buying a jacket turned out to be a disappointment. Lightning breaks after a while.",
#     "Unsatisfactory quality: The jacket I purchased does not meet my expectations. Lightning breaks after a while.",
#     "Insufficient durability: The zipper on the jacket was not as durable as in the photo. It breaks down after a while.",
#     "Inconsistency with the description: The purchase of the jacket was unsuccessful. Lightning breaks after a while.",
#     "Unsatisfactory fabric quality: The jacket I bought did not meet my expectations. Lightning breaks after a while.",
#     "Insufficient strength of the zipper: The zipper on the jacket was not as strong as on the website. It breaks down after a while.",
#     "Not meeting expectations: The jacket I purchased does not meet my expectations. Lightning breaks after a while.",
#
#     "Insufficient delivery speed: The purchase of the jacket turned out to be a disappointment due to the slow delivery.",
#     "Unsatisfactory delivery speed: The jacket I bought was not as promised. The delivery took too long.",
#     "Not meeting expectations: The purchase of the jacket was unsuccessful due to slow delivery.",
#     "Insufficient delivery speed: The jacket I purchased does not meet my expectations. The delivery took too long.",
#     "Unsatisfactory delivery speed: The purchase of the jacket turned out to be a disappointment due to the slow delivery.",
#
#     "Impressive design: A jacket with a beautiful design that I really liked.",
#     "Stylish and beautiful: The jacket turned out to be stylish and beautiful, as promised.",
#     "Original design: A jacket with an original design that I really liked.",
#     "Beautiful and stylish: The jacket turned out to be beautiful and stylish, as promised.",
#     "Impressive Style: A jacket with an impressive style that I really liked."
# ]
