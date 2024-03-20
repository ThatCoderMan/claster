import numpy as np
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from tqdm import tqdm

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


class Embedding:

    def __init__(self, data: list[str], model: str = 'BAAI/bge-base-en-v1.5'):
        self.model = HuggingFaceEmbedding(model)
        self.data = data

    def create_embeddings(self) -> np.array:
        print('Creating embeddings...')
        embeddings = np.array([np.array(self.model.get_text_embedding(item)) for item in tqdm(self.data)])
        print(f'Got dataset with {len(embeddings)} items with {len(embeddings[0])} dimensional measurement')
        np.save('file', embeddings)
        return embeddings

    @staticmethod
    def load() -> np.array:
        return np.load('file.npy')
