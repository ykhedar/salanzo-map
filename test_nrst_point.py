#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import time

# Generate random x,y points
from scipy.spatial import KDTree


def create_test_file(num_of_points, outfile_name):
    N = num_of_points
    outfile = outfile_name
    pts = num_of_points*np.random.random((N, 2))
    np.savetxt(fname=outfile, X=pts, delimiter=",")


def read_test_file(filename):
    data = np.loadtxt(fname=filename, delimiter=",")
    print(type(data), data.shape)
    print(data)
    return data, data.shape[0]


def plot_points(all_points, pt_to_query, nrst_pt, radius):
    plt.plot(all_points[:, 0], all_points[:, 1], '.')
    plt.plot(pt_to_query[0], pt_to_query[1], color='green', marker='o', markersize=6)
    plt.plot(nrst_pt[0], nrst_pt[1], color='red', marker='o', markersize=6)

    plt.xlim(pt_to_query[0]-radius, pt_to_query[0]+radius)
    plt.ylim(pt_to_query[1]-radius, pt_to_query[1]+radius)
    plt.show()


def kdtree_method(pts, pt_to_query):
    # Create a KD Tree
    tree = KDTree(pts)
    answer_floats, answer_int = tree.query(np.array(pt_to_query), k=2)
    nrst_pt = pts[answer_int[-1]]
    return nrst_pt


def rtree_method():
    pass


def main():
    create_test_file(num_of_points=20000, outfile_name="data/test.csv")
    pts, N = read_test_file("data/test.csv")

    # Draw a random point from the point list
    index = np.random.randint(low=0, high=N)
    pt_to_query = pts[index]

    # Method 1: KDTree based nearest neighbour search
    time1 = time.time()
    nrst_pt = kdtree_method(pts, pt_to_query)
    time2 = time.time()
    print("Time for KDTree: ", time2-time1)

    # Method 2: RTRee based nearest neighbour search


    # Select a sub-region around query point to plot.
    RADIUS = 2000
    plot_points(pts, pt_to_query, nrst_pt, RADIUS)


main()