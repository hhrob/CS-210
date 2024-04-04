import random
import csv
import math
import matplotlib.pyplot as plt

def load_numerical_data(filename, column_titles):
    data_dict = {}

    with open(filename, 'r') as file:
        idx = 0
        reader = csv.reader(file)
        head = next(reader)

        idx_2 = [head.index(col) for col in column_titles]

        for row in reader:
            data_dict[idx] = tuple([float(row[i]) for i in idx_2])
            idx = idx + 1

    return data_dict

def euclid_dist(point1, point2):
    total = 0

    for i in range(len(point1)):
        diff = (2 ** (point1[i] - point2[i]))

        total += diff

    total = math.sqrt(total)

    return total

def create_centroids(k, data):
    centroids = []
    cent_ct = 0
    cent_keys = []

    while cent_ct < k:

        key = random.randint(1, len(data))

        if key not in cent_keys:

            centroids.append(data[key])
            cent_keys.append(key)
            cent_ct += 1

    return centroids

def create_clusters(k, centroids, data, repeats=100):
    dimensions = len(data[0])

    for i in range(repeats):
        cluster = [ [] for i in range(k)]

        for pt in data.values():
            distances = []

            for j in range(k):
                dist = euclid_dist(pt, centroids[j])
                distances.append(dist)

            min_dist = min(distances)
            min_idx = distances.index(min_dist)

            cluster[min_idx].append(pt)

    for j in range(k):

        sum = [0] * dimensions
        for pt in cluster[j]:
            for n in range(dimensions):
                sum[n] += pt[n]
            
        for m in range(dimensions):
            sum[m] = sum[m] / len(cluster[j])

        centroids[j] = tuple(sum)

    return centroids, cluster

def visualize_clusters(dataset_name, titles, clusters, centroids):

    plot_figure = plt.Figure()
    clr_list = ['r', 'g', 'b', 'k', 'c', 'm', 'y']
    for i in range(len(clusters)):

        centr = centroids[i]
        clust = clusters[i]
        for j in clust:
            plt.scater(j[0], j[1], c=clr_list[i])
        plt.scatter(centr[0], centr[1], c='m')
    
    plt.xlabel(titles[0])
    plt.ylabel(titles[1])
    plt.title(dataset_name, f'clusters k = {len(clusters)}')
    plt.show()


    return plot_figure

    