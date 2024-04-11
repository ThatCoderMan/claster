from sentence_transformers import SentenceTransformer

model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
sentence = 'Мама мыла раму'

embedding = model.encode(sentence)
print(len(embedding))