import gensim.downloader as api
import time
from nltk.cluster import KMeansClusterer
import nltk

model = api.load("glove-twitter-25")  # download the model and return as object ready for use
print(model.similarity('dog', 'puppy'))

X = model[model.vocab]

NUM_CLUSTERS=3
kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25)
assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
print(assigned_clusters)
# output: [0, 2, 1, 2, 2, 1, 2, 2, 0, 1, 0, 1, 2, 1, 2]
