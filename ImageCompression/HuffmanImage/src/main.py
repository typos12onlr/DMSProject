import utils.file_handling as file_handling
import utils.huffman_coding as huffman_coding
import os


image_path="ImageCompression/HuffmanImage/src/Cat.jpg"

 #input("Image Path: ")  # IO/Inputs/Cat.jpg
image_bit_string = file_handling.read_image_bit_string(image_path)
print("read file")

compressed_image_bit_string = huffman_coding.compress(image_bit_string)
print("compressed ")

file_handling.write_image(compressed_image_bit_string,
                          "ImageCompression/HuffmanImage/src/compressed.bin")
print("made bin")
print("Compression Ratio (CR):",
      len(image_bit_string) / len(compressed_image_bit_string))

decompressed_image_bit_string = huffman_coding.decompress(
    compressed_image_bit_string)

print("decompressed")

file_handling.write_image(decompressed_image_bit_string,
                          "ImageCompression/HuffmanImage/src/decompressed.jpg")

print("wrote decompressed")