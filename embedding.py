import numpy as np
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from tqdm import tqdm


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
        print('Loading data...')
        embeddings = np.load('file.npy')
        print(f'Got dataset with {len(embeddings)} items with {len(embeddings[0])} dimensional measurement')
        return embeddings
