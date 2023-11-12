from utils.general_utils import *
from utils.k_means_utils import *
import os

inp_path=input("Enter image path: ")
inp_size=os.path.getsize(inp_path)
original_img = plt.imread(inp_path)
split=inp_path.split("/")

out_path="Images/compressed_"+split[-1]

original_img = original_img / 255

X_img = np.reshape(original_img, (original_img.shape[0] * original_img.shape[1], 3))


#Compressing
K = 16 
max_iters = 10              

# Using the function you have implemented above. 
initial_centroids = kMeans_init_centroids(X_img, K) 

# Run K-Means - this takes a couple of minutes
centroids, idx = run_kMeans(X_img, initial_centroids, max_iters) 

# Represent image in terms of indices
X_recovered = centroids[idx, :] 

# Reshape recovered image into proper dimensions
X_recovered = np.reshape(X_recovered, original_img.shape) 

compressed=X_recovered*255

plt.imsave(out_path,compressed)
out_size=os.path.getsize(out_path)

print(f"Compression ratio = {format(out_size/inp_size,'.2f')}")