import sys
from .clusterer import Clusterer


def run():
    filename = r'test_data_files\sample.log'
    clusterer = Clusterer()
    contents = []
    with open(filename, 'r') as f:
        for line in f:
            clusterer.cluster(line)
    
    clusterer.clusters.sort(key = lambda x:-x[1])
    for cl in clusterer.clusters:
        print(cl[1], ' '.join(map(str, cl[0])))
    pass
