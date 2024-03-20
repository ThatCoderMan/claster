from sklearn.cluster import DBSCAN
from sklearn.manifold import TSNE
from umap import UMAP

class Cluster:

    def __init__(
            self,
            embeddings: list[list[float]],
            n_components: int = 2,
            perplexity: int = 10,
            learning_rate: int = 1000,
            eps: float = 2500,
            min_samples: int = 3
    ):
        self.embeddings = embeddings
        # self.tsne = TSNE(n_components=n_components, perplexity=perplexity, learning_rate=learning_rate)
        self.tsne = UMAP(n_components=n_components)
        self.dbscan = DBSCAN(eps=eps, min_samples=min_samples)

    def create_projection(self):
        print('Creating projection...')
        return self.tsne.fit_transform(self.embeddings)

    def create_clusters(self, projection):
        print('Creating clusters...')
        return self.dbscan.fit(projection)
