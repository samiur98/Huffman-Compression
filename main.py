from HuffmanEncoder import *
from HuffmanDecoder import *
import sys

#Main Program used to run the Huffman Compressor using the command line interface.

#In order to encode a text file follow the following format in the terminal:
# python3 main.py encode [Name of file to be encoded].txt [Name of encoded file].txt

#In order to decode a text file follow the following format in the terminal:
# python3 main.py decode [Name of file to be decoded].txt [Name of decoded file].txt


#Main Program
arguments = sys.argv
encoder = HuffmanEncoder()
decoder = HuffmanDecoder(encoder)
if len(sys.argv) != 4:
    print ("Incorrect Input Format")
    exit(1)

if sys.argv[1] == "encode":
    encoder.encode(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "decode":
    decoder.decode(sys.argv[2], sys.argv[3])
else:
    print ("Incorrect Input Format")
