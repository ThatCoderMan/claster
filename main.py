from collections import Counter

import numpy as np

from create_dataset import results

from embedding import Embedding
from cluster import Cluster
from itertools import chain
from plot import Plot

data = list(chain(*results))
# enb = Embedding(data).create_embeddings()
enb = Embedding(data).load()
clustering = Cluster(enb, perplexity=100, eps= 0.17, min_samples=5)
projection = clustering.create_projection()
cluster = clustering.create_clusters(projection)

plot = Plot(cluster, projection)
plot.create_plot()
# plot.save(f'images/{perplexity}.png')
plot.show()