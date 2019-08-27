from HuffmanNode import *
class HuffmanDecoder:
    #Class that decodes an encoded file that has been encoded by a Huffman Encoder.

    def __init__(self, encoder):
        self.encoder = encoder

    def __str__(self):
        return "HuffmanDecoder"

    def decode(self, inFile, outFile):
        #Method that decodes an encoded file and revives the original text file.
        print ("decode")
        try:
            file = open(inFile, 'r')
            splitList = file.readlines()
            file.close()
            if len(splitList) == 1:
                #Case where encoded file only has header.
                values = splitList[0].split(" ")
                character = chr(int(values[0]))
                frequency = int(values[1])
                counter = 0
                outPut = open(outFile, 'w')
                while(counter < frequency):
                    outPut.write(character)
                    counter = counter + 1
                outPut.close()
            else:
                #Case where encoded file has header and huffman code.
                nodeList = self.parseHeader(inFile)
                tree = self.encoder.buildTree(nodeList)
                outPut = open(outFile, 'w')
                code = splitList[1]
                node = tree
                for character in code:
                    if character == '0':
                        node = node.left
                    else:
                        node = node.right
                    if (node.left == None) and (node.right == None):
                        outPut.write(node.getCharacter())
                        node = tree
                outPut.close()
        except IOError:
            print ("Sorry File Does not Exist")
        except ValueError:
            print ("File provided is not Formatted Correctly")

    def parseHeader(self, inFile):
        #Returns a HuffmanNode representing the characters in the encoded file.
        frequencyList = []
        file = open(inFile, 'r')
        splitList = file.readlines()
        file.close()
        splitList[0] = splitList[0][:-1]
        headerList = splitList[0].split(" ")
        for i in range(0, len(headerList), 2):
            frequencyList.append(Node(chr(int(headerList[i])), int(headerList[i + 1])))
        return frequencyList
