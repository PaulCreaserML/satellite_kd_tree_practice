import numpy as np
from scipy.spatial import KDTree

def demonstrate_gcp_matching():
    """
    Demonstrates using a k-d tree to find the nearest Ground Control Point (GCP)
    for a set of detected features in a satellite image.
    """

    # 1. --- Sample Data ---
    # Imagine these are (lat, lon) or (x, y) coordinates.
    # This is your reference catalog of known ground locations.
    ground_control_points = np.array([
        [25.7, 80.2],
        [26.1, 81.3],
        [25.9, 80.7],
        [26.5, 81.1],
        [25.5, 80.9],
        [26.8, 80.5]
    ])
    print("Reference Ground Control Points (GCPs):")
    print(ground_control_points)
    print("-" * 30)

    # These are the features detected in your new satellite image.
    # We need to find the closest known GCP for each of these points.
    detected_features = np.array([
        [25.72, 80.25],
        [26.48, 81.05],
        [25.51, 80.88]
    ])
    print("Detected Features in Image:")
    print(detected_features)
    print("-" * 30)


    # 2. --- Build the k-d Tree ---
    # We build the tree on the reference data (the GCPs) because this is the
    # dataset we will be searching through repeatedly.
    # Building the tree is a one-time, efficient pre-processing step.
    print("Building k-d tree from GCPs...\n")
    kdtree = KDTree(ground_control_points)


    # 3. --- Query the Tree ---
    # Now, we can query the tree to find the nearest neighbor for each of
    # our detected features. The query is very fast.
    # k=1 means we want to find the 1 closest neighbor.
    # The query returns two arrays:
    # distances: The distance to the nearest neighbor.
    # indices: The index of that neighbor in the original `ground_control_points` array.
    distances, indices = kdtree.query(detected_features, k=1)


    # 4. --- Display the Results ---
    print("Matching Results:")
    for i in range(len(detected_features)):
        detected_point = detected_features[i]
        closest_gcp_index = indices[i]
        closest_gcp = ground_control_points[closest_gcp_index]
        distance = distances[i]

        print(
            f"  - Detected Feature: {detected_point}\n"
            f"    -> Closest GCP:    {closest_gcp} (Index: {closest_gcp_index})\n"
            f"    -> Distance:       {distance:.4f}\n"
        )

if __name__ == "__main__":
    demonstrate_gcp_matching()

