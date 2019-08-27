from HuffmanEncoder import *
from HuffmanDecoder import *
def test():
    encoder = HuffmanEncoder()
    decoder = HuffmanDecoder(encoder)
    encoder.encode("basic.txt", "basicEncode.txt")
    decoder.decode("basicEncode.txt", "basicDecode.txt")
    encoder.encode("illenium.txt", "illeniumEncode.txt")
    decoder.decode("illeniumEncode.txt", "illeniumDecode.txt")
    encoder.encode("empty.txt", "patsy.txt")
    encoder.encode("single.txt", "singleEncoded.txt")
    decoder.decode("singleEncoded.txt", "singleDecoded.txt")
test()