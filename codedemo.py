import doctest

def two_lists_to_dict(list1, list2):
    '''
    >>> two_lists_to_dict(['Ten', 'Twenty'], [10, 20])
    {'Ten': 10, 'Twenty': 20}
    '''
    ret_dict = {}
    for i in range(len(list1)):
            ret_dict[list1[i]] = list2[i]
            

    return ret_dict

print(two_lists_to_dict(["Ten", 'Twenty'], [10, 20]))

def two_lists_to_dict_comp(list1, list2):
    return {list1[i]: list2[i] for i in range(len(list1))}

print(doctest.testmod())
import random
import math
import csv
import matplotlib.pyplot as plt

def load_numerical_data(filename: str, column_titles: list) -> dict:
    """Load data from a CSV file and return a dictionary with keys being the
    row number and values as tuples of the data in each row, converted to float.

    Args:
        filename: The name of the CSV file to load.
        column_titles: A list of columns to load.

    Returns:
        A dictionary where each element corresponds to a data point, with keys 
        corresponding to the row number and values as a tuple of floats.

    Example:
        If column_titles = ['Col1', 'Col3'], and the CSV file has the following data:
            Col1, Col2, Col3
             2.4,  5.6,  7.8
            10.0, 42.5, -3.2
        Then the return value will be:
            {0: (2.4, 7.8), 1: (10, -3.2)}
    """
    data = {}
    with open(filename, 'r') as f:
        index = 0
        csvreader = csv.reader(f)
        header = next(csvreader)
        for col_title in column_titles:
            if col_title not in header:
                raise ValueError(f'{col_title} not in header of {filename}')
        indices = [header.index(title) for title in column_titles]
        for row in csvreader:
            if len([i for i in indices if row[i] == '']) > 0:
                continue
            data[index] = tuple([float(row[i]) for i in indices])
            index += 1
    return data

def euclid_dist(point1: tuple, point2: tuple) -> float:
    """Compute the Eucledian distance between two points represented as tuples.
    Listing 7.1 in PPC, with modifications for compliance to PEP8

    Args:
        point1: A tuple representing a point in n-dimensional space.
        point2: A tuple representing a point in n-dimensional space.

    Returns:
        float: The Euclidean distance between the two points.
    
    Example:
        euclid_dist((1, 2.5), (2.1, 4)) should return 1.86 (approximately).

    >>> round(euclid_dist((1, 2.5), (2.1, 4)), 2)
    1.86
    >>> round(euclid_dist((0, 0), (2, 2)), 2)
    2.83
    """
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff
    return math.sqrt(total)


def create_centroids(k: int, data: dict) -> list:
    """Create k centroids for the data.

    Args:
        k: The number of centroids to create.
        data: A dictionary where each element corresponds to a data point, with keys
            corresponding to the row number and values as a tuple of floats.

    Returns:
        list: a list of centroids, each centroid is a tuple of floats.
    """
    centroids = []
    centroid_count = 0
    centroid_keys = []  # list of unique keys
    while centroid_count < k:
        # Pick a random key from the data, this will be the centroid
        rand_key = random.randint(1, len(data))
        if rand_key not in centroid_keys:
            centroids.append(data[rand_key])
            centroid_keys.append(rand_key)
            centroid_count += 1
    return centroids

def create_clusters(k: int, centroids: list, data: dict, repeats=100) -> list:
    """Create clusters using the k-means algorithm
    From Listing 7.8, modified for Project 8 data structures and requirements.
    Args:
        k:
        centroids:
        values: list of tuples
        repeats:

    Returns:
        dict: a list of clusters
    """
    # Repeat until the centroids no longer change
    for a_pass in range(repeats):
        clusters = [ [] for i in range(k)]

        # Calculate the distance to centroid for each data point
        for point in data.values():
            distances = []
            # Compute distance between all centroids and this value
            for cluster_index in range(k):
                dist_to_centroid = euclid_dist(point, centroids[cluster_index])
                distances.append(dist_to_centroid)
            # Find the index of the centroid closest to this point
            min_distance = min(distances)
            min_index = distances.index(min_distance)

            # Add this point to the cluster with the closest centroid
            clusters[min_index].append(point)

        # Calculate the new centroids
        dimensions = len(data[0])
        for cluster_index in range(k):
            # Compute the new centroid for this cluster
            sums = [0] * dimensions
            for point in clusters[cluster_index]:  # point is a tuple
                for index in range(dimensions):
                    sums[index] += point[index]
            for index in range(dimensions):
                sums[index] = sums[index] / len(clusters[cluster_index])

            centroids[cluster_index] = tuple(sums)

    return clusters, centroids


def visualize_clusters(dataset_name: str, titles: list, clusters: list,
                       centroids: list) -> plt.Figure:
    """Visualize the clusters and centroids. Use a different color for each cluster. 
    Args: 
        dataset_name: The name of the dataset
        titles: list of string column titles
        clusters: list of lists of tuples
        centroids: list of tuples
    Returns:
        matplotlib.pyplot.Figure: The figure object
    """

    fig = plt.Figure()
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    for cluster_index in range(len(clusters)):
        cluster = clusters[cluster_index]
        centroid = centroids[cluster_index]
        for point in cluster:
            plt.scatter(point[0], point[1], c=colors[cluster_index])
        plt.scatter(centroid[0], centroid[1], c='k', marker='*')
    plt.xlabel(titles[0])
    plt.ylabel(titles[1])
    plt.title(f'{dataset_name} clusters k={len(clusters)}')
    plt.savefig(f"clusters_{dataset_name}_{'_'.join(titles)}.png")
    plt.show(block=False)
    return fig


def main():
    """ Main driver for the program."""

    # Specifies the files and columns to analyze
    datasets = {('earthquakes', ('latitude', 'longitude')): 5,
                ('earthquakes', ('depth', 'mag')): 5,
                ('cis210_scores', ('Projects', 'Exams')): 5}

    # Compute clusters for all datasets
    for (dataset, titles), k in datasets.items():
        print(f'\nDataset: {dataset} {titles}')
        data = load_numerical_data(dataset + '.csv', column_titles=titles)
        centroids = create_centroids(k, data)
        print("Initialized the centroids.")
        clusters, centroids = create_clusters(k, centroids, data)
        print("\nCreated the clusters.")
        visualize_clusters(dataset, titles, clusters, centroids)
        print("Visualized the clusters.")


if __name__ == '__main__':
    main()
