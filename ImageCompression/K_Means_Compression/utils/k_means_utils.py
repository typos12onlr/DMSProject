import numpy as np
import matplotlib.pyplot as plt
from utils.general_utils import *



def find_closest_centroids(X, centroids):

    #Computes the centroid memberships for every example


    # Set K
    K = centroids.shape[0]

    # You need to return the following variables correctly
    idx = np.zeros(X.shape[0], dtype=int)

   
    for i in range(len(idx)):
        distances=[]
        for j in range(centroids.shape[0]):
            
            
            distances.append(np.linalg.norm(X[i]-centroids[j]))

        idx[i]=distances.index(min(distances))

    
    return idx

def compute_centroids(X, idx, K):
    
    # Returns the new centroids by computing the means of the 
    # data points assigned to each centroid.
    
    
    # Useful variables
    m, n = X.shape
    
    # You need to return the following variables correctly
    centroids = np.zeros((K, n))
    
    
    for i in range(K):
        points=X[idx==i]

        centroids[i]=np.mean(points,axis=0)
    
    return centroids

def run_kMeans(X, initial_centroids, max_iters=10, plot_progress=False):
    
    # Runs the K-Means algorithm on data matrix X, where each row of X
    # is a single example
    
    
    # Initialize values
    m, n = X.shape
    K = initial_centroids.shape[0]
    centroids = initial_centroids
    previous_centroids = centroids    
    idx = np.zeros(m)
    print("Compressing image...")
    # Run K-Means
    for i in range(max_iters):
        
        #Output progress
        #print("K-Means iteration %d/%d" % (i, max_iters-1))
        
        # For each example in X, assign it to the closest centroid
        idx = find_closest_centroids(X, centroids)
        
        # Optionally plot progress
        if plot_progress:
            plot_progress_kMeans(X, centroids, previous_centroids, idx, K, i)
            previous_centroids = centroids
            
        # Given the memberships, compute new centroids
        centroids = compute_centroids(X, idx, K)
    #plt.show() 
    return centroids, idx

def kMeans_init_centroids(X, K):

    # This function initializes K centroids that are to be 
    # used in K-Means on the dataset X

    
    # Randomly reorder the indices of examples
    randidx = np.random.permutation(X.shape[0])
    
    # Take the first K examples as centroids
    centroids = X[randidx[:K]]
    
    return centroids