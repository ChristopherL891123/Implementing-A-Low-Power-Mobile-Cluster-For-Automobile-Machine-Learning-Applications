"""This script is for the purposes of predicting what a car will do based on pictures
Predictions will be made via a K-means model from scikit learn trained on the CCD Carcrash dataset"""


#Imports
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import numpy as np
import os
import cv2 as cv
from sklearn.metrics import silhouette_score

#Data loading

#Step 1: Load the folder of images

# Specify the path to the folder containing your JPG images
folder_path = 'C:\\Users\\begin\\PycharmProjects\\image_clustering\\venv\\Data'

image_data = []
counter = 0

#Step 2: Iterate through each image in the folder and turn it into an array

#Loop through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        # Read the image using OpenCV
        image = cv.imread(os.path.join(folder_path, filename))
        # Convert the image to grayscale (optional) and reshape it
        #image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # Flatten the image into a 1D array
        image = image.flatten()
        image_data.append(image)
        counter+= 1
        print(counter)

#Step 3: Put all of those arrays together for one big array I can fit the model on

# Convert the list of image arrays to a single NumPy array
image_data = np.array(image_data)

#Attempting to reduce the dimensionality of the data so the clusters are less linear
# Create a PCA instance with the desired number of components (e.g., 2 for a 2D visualization)
n_components = 2
pca = PCA(n_components=n_components)

# Fit the PCA model to your image data and transform the data to the reduced dimension
image_data_pca = pca.fit_transform(image_data)

#Trains the model
kmeans = KMeans(n_clusters=10, init = 'random', n_init=100).fit(image_data_pca)

#Create a DBSCAN instance
#dbscan = DBSCAN(eps=0.5, min_samples=5)

# Fit the DBSCAN model to your data
#dbscan.fit(image_data)

#Let's graph the clusters
# Get cluster assignments and cluster centers
cluster_assignments = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

# Extract the labels assigned to each data point (clusters and noise are labeled)
#labels = dbscan.labels_

# Create a scatter plot of the original, unfiltered clusters
plt.figure(figsize=(10, 10))



# Scatter plot data points with different colors for each cluster
for i in range(kmeans.n_clusters):
    plt.scatter(image_data_pca[cluster_assignments == i, 0], image_data_pca[cluster_assignments == i, 1], label=f'Cluster {i}', s = 10)

# Plot cluster centers as red X markers
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='X', s=100, label='Cluster Centers')


"""
# Plot the data points color-coded by DBSCAN cluster
plt.scatter(image_data[:, 0], image_data[:, 1], c=labels, cmap='inferno')

# Plot noise points as black
plt.scatter(image_data[labels == -1, 0], image_data[labels == -1, 1], c='red', marker='x', s=50)"""
plt.title('K-Means Clustering')
plt.legend()
plt.show()

# Define a range of values for the number of clusters (k)
k_values = range(1, 11)
inertia_values = []

# Initialize a dictionary to store silhouette scores for each K
silhouette_scores = {}

# Calculate the inertia (within-cluster sum of squares) for different values of k
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto")
    kmeans.fit(image_data_pca)
    inertia_values.append(kmeans.inertia_)
    silhouette_avg = silhouette_score(image_data_pca, cluster_assignments)
    silhouette_scores[k] = silhouette_avg

# Create an elbow graph to determine optimum number of clusters
plt.figure(figsize=(8, 6))
plt.plot(k_values, inertia_values, marker='o', linestyle='-')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

#Performance metrics

# Calculate distances from each data point to the nearest cluster center
distances = np.min(cdist(image_data_pca, cluster_centers, 'euclidean'), axis=1)

# Calculate the average (mean) distance
average_distance = np.mean(distances)
print(f"The average distance between a data point to its nearest cluster is: {average_distance}")

#Silhouette Score
# Find the K with the highest Silhouette Score
best_k = max(silhouette_scores, key=silhouette_scores.get)

# Print the Silhouette Scores for each K
for k, score in silhouette_scores.items():
    print(f"K={k}, Silhouette Score: {score}")

# Print the best K and its corresponding Silhouette Score
print(f"Best K: {best_k}, Best Silhouette Score: {silhouette_scores[best_k]}")


#Predict based on new data
#This is where you put the pictures you took to predict which cluster they'd fall into.
#new_data_labels = kmeans.predict(new_data)#Put your new data here
