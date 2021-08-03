import sys
import os
from .clusterer import Clusterer
from .input import Input
from .output import Output


def run():
    # Get input from console
    inp = Input()
    options = inp.get_args()
    
    filename = options['file']
    if(filename == '-'):
        inp.print_help()
        return
    
    # Initialize clusterer object (main algorithm)
    max_dist = options['max_dist']
    clusterer = Clusterer(max_dist=max_dist)

    filename = filename[0]
    filename = os.path.join('', filename)

    # Run the algorithm to cluster data
    with open(filename, 'r') as content:
        for line in content:
            clusterer.make_cluster(line)

    clusters = clusterer.result()

    # Check if sorted in ascending or descending
    sortby = options['sorted']
    if sortby == 'asc':
        clusters.sort(key = lambda x:x[1])
    elif sortby == 'desc':
        clusters.sort(key = lambda x:-x[1])
    else:
        print('Invalid argument for sorted, defaulting to ascending order')

    # Output the results to the console
    output = Output()
    output.print_results(clusters)

    
