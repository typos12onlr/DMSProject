from huffman import HuffmanDecoding
import pickle
import easygui as eg 

fp=eg.fileopenbox()

fppkl=fp[:-3]+"pkl"


with open(fppkl,"rb") as fin:
    loaded_tree=pickle.load(fin)


with open(fp,"rb") as fin:
    data=fin.read()
    binary_data_str = ''.join(format(byte, '08b') for byte in data)

    text=HuffmanDecoding(binary_data_str,loaded_tree)

    fp2=fp[:-3]+"txt"
    with open(fp2,"w") as fout:
        fout.write(text)
    fp2=fp2.split("\\")[-1]
print(f"File has been decompressed to {fp2}")

