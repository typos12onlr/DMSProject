from utils.lzw import *
import cv2 as cv
import math
import matplotlib.pyplot as plt
import numpy as np
import pickle
import easygui as eg


img_path=eg.fileopenbox()

img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

# Calculate the entropy and maximum achievable compression ratio of the input image
#entropy, max_compression = f(img)

# Get the height and width of the input image
height, width = img.shape

# Get the block size for LZW encoding
block_size = 16

# Get the maximum dictionary size for LZW encoding
max_dict_size = 1024

# Encode the input image using LZW encoding and save the encoded data to a file
encoded_img, max_dict_filled = lzw_encoder(img, block_size, max_dict_size)

extra_info=[[height,width,block_size,max_dict_size]]

extra_info.extend(encoded_img)

with open("compressed.pkl", "wb") as pickle_file:
        pickle.dump(extra_info, pickle_file)

with open("compressed.pkl","rb") as fin:
    loaded=pickle.load(fin)

not_extra_info=loaded[0]
encoded_img=loaded[1:]

decoded_img = lzw_decoder(encoded_img, height, width, block_size, max_dict_size)
outpath=img_path.split("\\")
temp=outpath[-1]
outpath_final="\\".join(outpath[:-1])+"\\decompressed"+temp
#images\grayscale\1.png

plt.imsave(outpath_final, decoded_img,cmap="gray")