# K-D Tree for Ground Control Point (GCP) Matching
This repository contains a Python script that demonstrates the use of a k-d tree for efficiently matching detected features in a satellite image to a catalog of known Ground Control Points (GCPs).

## Problem Statement
In satellite imagery processing, a common task during geometric correction is to match features detected in a new image (e.g., road intersections, coastlines) to known, real-world coordinates from a reference catalog. This process is crucial for accurately georeferencing the image.

Given a large set of detected features and an even larger reference catalog of GCPs, a brute-force approach of comparing every feature to every GCP to find the closest one is computationally expensive, with a complexity of O(N*M), where N is the number of features and M is the number of GCPs.

## Solution: The K-D Tree
A k-d tree (k-dimensional tree) is a space-partitioning data structure for organizing points in a k-dimensional space. It allows for very fast nearest-neighbor searches.

By building a k-d tree from the reference GCP catalog, we can reduce the average time complexity of finding the nearest neighbor for each detected feature to O(log M), which is a significant improvement for large datasets.

How the Script Works
The kdtree_gcp_matching.py script demonstrates this process with a simple example:

Sample Data: It initializes two sets of 2D coordinates:

ground_control_points: A NumPy array representing the reference catalog of known locations.

detected_features: A NumPy array representing the points detected in a new satellite image.

Build Tree: It uses scipy.spatial.KDTree to build a k-d tree from the ground_control_points. This is an efficient, one-time preprocessing step.

Query Tree: The script then queries the tree with the detected_features to find the single nearest neighbor (k=1) for each point.

Display Results: Finally, it iterates through the results, printing each detected feature, its closest matching GCP from the catalog, the index of that GCP, and the Euclidean distance between them.

## Requirements
To run this script, you need Python and the following libraries:

NumPy: For numerical operations and array handling.

SciPy: For the KDTree implementation.

You can install them using pip:

pip install numpy scipy

## Usage
Simply run the script from your terminal:

python kdtree_gcp_matching.py

Example Output

Running the script will produce the following output, showing the matches found:

Reference Ground Control Points (GCPs):
[[25.7 80.2]
 [26.1 81.3]
 [25.9 80.7]
 [26.5 81.1]
 [25.5 80.9]
 [26.8 80.5]]
------------------------------
Detected Features in Image:
[[25.72 80.25]
 [26.48 81.05]
 [25.51 80.88]]
------------------------------
Building k-d tree from GCPs...

Matching Results:
  - Detected Feature: [25.72 80.25]
    -> Closest GCP:    [25.7 80.2] (Index: 0)
    -> Distance:       0.0539

  - Detected Feature: [26.48 81.05]
    -> Closest GCP:    [26.5 81.1] (Index: 3)
    -> Distance:       0.0539

  - Detected Feature: [25.51 80.88]
    -> Closest GCP:    [25.5 80.9] (Index: 4)
    -> Distance:       0.0224


