import io
from utils.data_compression import *
from utils.data_decompressor import *
import easygui as eg

file = eg.fileopenbox()
myfile = open(file)
info = str(myfile.readlines())
compressing(info)
print('Decompressing the file')
decompressing()



 
 
 




