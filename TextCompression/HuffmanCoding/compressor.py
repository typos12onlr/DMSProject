from huffman import *
import os
fp=eg.fileopenbox()
fp_out=''.join(fp.split('.')[:-1])+"compressed.bin"
    

    
#print(fp,fp_out)
with open(fp,"r") as fin:
    the_data = fin.read()
#print(the_data)  
encoding, the_tree = HuffmanEncoding(the_data)  
#print("Encoded output", encoding)  
#print("Decoded Output", HuffmanDecoding(encoding, the_tree))
# Binary data as a string of 1s and 0s
binary_data_str = encoding

# Convert the binary string to bytes
binary_data = bytes(int(binary_data_str[i:i+8], 2) for i in range(0, len(binary_data_str), 8))

# Specify the file path
file_path = fp_out

# Open the file in write binary mode ('wb')
try:
    with open(file_path, "wb") as binary_file:
        # Write the binary data to the file
        binary_file.write(binary_data)
        print("Data has been successfully written to the binary file.")
except IOError as e:
    print(f"Error: {e}")


fppkl=fp_out[:-3]+"pkl"



with open(fppkl,'wb') as fin:
    pickle.dump(the_tree,fin)



# Get the file size in bytes
file_size_in = os.path.getsize(fp)
file_size_out=os.path.getsize(fp_out)

print(f"Compressed file is {round(100*file_size_out/file_size_in)} percent the size of input file")