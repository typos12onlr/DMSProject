import io
import pickle


def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            
            dict_size += 1
            w = c

    #Output the new Dictionary.       
    newDictionary = list(dictionary.items())

       
    #Output the code for w.
    if w:
        result.append(dictionary[w])
    return result

def compressing(string):
    
    print("Compressing Data ")
    compressed = compress(string)
    # print ("Compressed output: ",compressed)
    
    with open("output.pkl", "wb") as pickle_file:
        pickle.dump(compressed, pickle_file)


    # print("\n")
    # with open("output.pkl", "rb") as fin:
    #     loaded=pickle.load(fin)
    
    # print("Decompressing Data >>>")
    # # decompressed = decompression.decompress(loaded)
    # # with open('decompressed.txt', 'w') as fout:
    # #     data_list = eval(decompressed)
    # #     for item in data_list:
    # #         fout.write(item)

    # # print ("Decompressed output: ",decompressed)
    # print("\n")

    # print ("COMPARE:")
    # if string == decompressed:
    #     print("Successfully Done")

    # else:
    #     print("Not done!")
    #     print("\n")