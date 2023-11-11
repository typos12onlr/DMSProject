# Shrinkr- A file compression tool 
## Introduction

We live in a fast growing computing world with a need of safe, optimised and consistent communication systems which require a lot of data to be transferred, large-sized or small.
As the amount of data that we make digital increases, the problem of storage of data increases considerably, increasing the cost of running systems or businesses that deal with huge amount of data.
Here is where data compression comes into play. Compression of data can be a huge optimisation in the case of data transfer and storage as it reduces the number of bits to be transferred, thus aiding in quicker and more efficient data transfer.
Our projects aims at exploring some lossy or lossless compression techniques like Huffman Coding and several others to apply compression to images.

## Objectives

To implement Binary trees to compress generic textual data.
To implement Binary Trees and Matrices for performing  image compression.
To use Vector Quantization to down sample and the later reproduce the input image to avoid loss if image data, at the same time compressing it.

## Planned Methodology

1) Binary Minimum-Heap Tree (BMHT) for Huffman Coding:
Symbol Frequency Analysis: Image pixel values analysis to determine the frequency of occurrence of each symbol (e.g., grayscale intensity values or color combinations).
Binary Minimum-Heap Tree: a BMHT is built over the concepts of Graph Theory, where each node in the tree would represent a symbol. The least frequent symbols would be closer to the roots of the BMHT.
Encoding: The BMHT is traversed to assign codes to the symbols which are derived from the route taken from the root to the node which represents the symbol.

2) Visual Pattern Vector Quantization (VPVQ): Vector Quantization (VQ) is an advanced compression technique that involves representing groups of similar data points (vectors) with a single representative vector.
Vectorization: VPVQ divides an image into segments, and each segment is represented by a vector (called a codeword) from a predefined codebook. The codebook contains a set of representative vectors that are obtained through techniques like clustering (e.g., k-means) or other optimization methods.
Run-Length Encoding: VPVQ can achieve higher compression ratios compared to simple techniques like RLE, but it requires more computational resources for encoding and decoding.

3) Interpolation Techniques for Image Resampling: Unlike traditional “compression”, resizing can be considered a form of compression when you're trying to represent an image with fewer pixels.
Downsampling: Using techniques like nearest-neighbour, bilinear, or bicubic interpolation when downsampling (reducing image size) or upsampling (increasing image size). These methods fill in missing pixel values based on nearby pixels using discrete mathematical principles.
Subpixel Accuracy: Some interpolation techniques consider subpixel accuracy to provide smoother resampling results. This involves estimating pixel values at fractional coordinates, which can be done using mathematical models.




