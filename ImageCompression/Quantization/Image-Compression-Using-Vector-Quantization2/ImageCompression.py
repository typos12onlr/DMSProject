#!/usr/bin/env python
# coding: utf-8

# <b>Introduction</b>
# 
# This project intend to use KMeans clustering to compress an image.This  technique is based on paper published by Gersho and Gray in 1992 . It works by clustering similar pixels and representing  pixels in a cluster by cluster centroid, collection of centroids is called codebook. The process is also called as Vector Quantization(VQ) and the process is used for various signal compression. 
# 
# <b>Data</b>
# 
# Data is an image of my college DTU.
# 
# 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import sklearn 
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import decomposition as dcmp
from sklearn import preprocessing as prep
from sklearn import cluster
import matplotlib.image as mpimg
from skimage.io import imread, imshow, imsave
import os


# In[2]:


#Loading the data
wing=imread("wing.jpg")
#Displaying the image
imshow(wing)


# In[3]:


# Making the image compatible with matplotlib 
# Matplotlib represent RGB from value 0 to 1
wing_f64=wing.astype(dtype=np.float64)/255
#Ensuring conversion did not significantly alter the image
imshow(wing_f64)


# In[4]:


# Determining the shape
wing_f64.shape


# In[5]:


wing_f64.shape[2]


# Unlike most dataset which is AxB matrix image is AxBxC matrix. In other word image is reprented by
# 
# (Height x Width x Pixels) matix. 

# In[15]:


# Extracting pixel from data set
px_d=[] #Temporarily store the pixel after grabbing the pixel at a locaton
px_v=[] # Warehousing the pixels

for i in range(wing_f64.shape[0]):
    for j in range(wing_f64.shape[1]):
      
      
        for k in wing_f64[i, j,:]:
           
            px_d.append(k)
           
        px_v.append(px_d) #Storing the the pixel 
        px_d=[] #Empties the pixel to grab a new one
        
# Turning the data into an array
vArray=np.array(px_v)

# Turning the araray into feature vector

vArrayDF=pd.DataFrame(vArray, columns=['r', 'g', 'b'])
vArrayDF #Displaying the pixels


# <b>K-Means Clustering</b>

# In[23]:


km=cluster.KMeans(init='k-means++', n_clusters=100, n_init=10)
km.fit(vArrayDF)
ym=km.predict(vArrayDF)


# <b> Generating codebook</b>

# In[ ]:





# In[24]:


codebook=km.cluster_centers_


# In[25]:


codebook


# <b>Building function to recreate image </b>

# In[26]:


def recreate_image(codebook, labels, y, x):
    #Creating all zero 3 dimension matrix. Information from codebook will be used to generate the pixels
    image = np.zeros((y, x, codebook.shape[1])) 
    label_idx = 0
    for i in range(y):
        for j in range(x):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image


# <b>Recreating the image</b>

# In[32]:


image=recreate_image(codebook, ym, wing_f64.shape[0], wing_f64.shape[1])
#Verifying the shape of image 
image.shape


# Shape of the new image is same as the original.So we will display the image
# 

# In[33]:


imshow(image)


# In[29]:


from PIL import Image
image = Image.fromarray((image * 255).astype(np.uint8))


# New image looks similar to the original image without significant loss of information.
# We will now save the image onthe disk for validation. We will call new image dtu_compressed.jpg

# In[30]:


image.save('wing_compressed.jpg')


# <b>Validation</b>

# In[31]:


origInal=os.path.getsize("wing.jpg")
compRessed=os.path.getsize("wing_compressed.jpg")
100*(origInal-compRessed)/origInal


# 
# 

# In[ ]:




