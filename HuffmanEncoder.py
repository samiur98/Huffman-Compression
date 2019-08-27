from HuffmanNode import *
class HuffmanEncoder:
    #Class responsible for encoding a text file based on the Huffman Greedy Algorithm.

    def __str__(self):
        return "Huffman Encoder"

    def encode(self, inFile, outFile):
        print ("encode")
        try:
            nodeList = self.parseInput(inFile)
            header = self.createHeader(nodeList)
            if len(nodeList) == 0:
                #Case where file is empty.
                print ("File is empty, there is nothing to encode.")
            elif len(nodeList) == 1:
                #Case where file only has one character, the header is only written to the encoded file.
                out = open(outFile, 'w')
                out.write(header)
                out.close()
            else:
                #Case where file is not empty and has more than one character.
                tree = self.buildTree(nodeList)
                characterList = self.characterListEncode(tree)
                file = open(inFile, 'r')
                out = open(outFile, 'w')
                out.write(header)
                out.write("\n")
                for line in file:
                    for character in line:
                        out.write(characterList[ord(character)])
                file.close()
                out.close()
        except IOError:
            print ("Sorry File Does not Exist")

    def parseInput(self, inFile):
        #Method that parses the input file and returns a list containing the Huffman Nodes of characters in the input file.
        counter = 0
        initialList = []
        finalList = []
        while (counter < 256):
            initialList.append(Node(chr(counter), 0))
            counter = counter + 1
        file = open(inFile, "r")
        for line in file:
            for charachter in line:
                node = initialList[ord(charachter)]
                node.setFrequency(node.getFrequency() + 1)
        file.close()
        for node in initialList:
            if node.getFrequency() > 0:
                finalList.append(node)
        return finalList

    def comesBefore(self, node1, node2):
        #Method that determines which node amongst the two arguments should come before during sorting.
        if node1.getFrequency() < node2.getFrequency():
            return node1
        elif node1.getFrequency() > node2.getFrequency():
            return node2
        else:
            if node1.getMinimum() < node2.getMinimum():
                return node1
            else:
                return node2

    def mergeSort(self, nodeList):
        #Method that sorts a list of Huffman Nodes using the merge sort algorithm.
        #Nodes are sorted from highest frequency to lowest frequency.
        if len(nodeList) > 1:
            mid = len(nodeList) // 2
            lefthalf = nodeList[:mid]
            righthalf = nodeList[mid:]
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if self.comesBefore(lefthalf[i], righthalf[j]) == lefthalf[i]:
                    nodeList[k] = lefthalf[i]
                    i = i + 1
                else:
                    nodeList[k] = righthalf[j]
                    j = j + 1
                k = k + 1
            while i < len(lefthalf):
                nodeList[k] = lefthalf[i]
                i = i + 1
                k = k + 1
            while j < len(righthalf):
                nodeList[k] = righthalf[j]
                j = j + 1
                k = k + 1
        return nodeList

    def buildTree(self, nodeList):
        #Method that build a HuffmanTree needed for Encoding.
        self.mergeSort(nodeList)
        while(len(nodeList) > 2):
            first = nodeList.pop(0)
            second = nodeList.pop(0)
            node = Node(None, first.getFrequency() + second.getFrequency())
            if self.comesBefore(first, second) == first:
                node.left = first
                node.right = second
            else:
                node.left = second
                node.right = first
            if node.getLeft().getMinimum() > node.getRight().getMinimum():
                node.setMinimum(node.getRight().getMinimum())
            else:
                node.setMinimum(node.getLeft().getMinimum())
            nodeList.append(node)
            self.mergeSort(nodeList)
        first = nodeList.pop(0)
        second = nodeList.pop(0)
        node = Node(None, first.getFrequency() + second.getFrequency())
        if self.comesBefore(first, second) == first:
            node.left = first
            node.right = second
        else:
            node.left = second
            node.right = first
        if node.getLeft().getMinimum() > node.getRight().getMinimum():
            node.setMinimum(node.getRight().getMinimum())
        else:
            node.setMinimum(node.getLeft().getMinimum())
        return node

    def characterListEncode(self, treeNode):
        #Method that returns a list representing the path needed to get to characters in the HuffmanTree, during the encoding process.
        #Path can be obtained by using the ASCII value of a character, as an index in the characterList.
        characterList = [""] * 256
        self.charachterListEncodeHelper(characterList, treeNode, "")
        return characterList

    def charachterListEncodeHelper(self, characterList, node, inString):
        #Helper Method for the characterListEncode method.
        if (node.getLeft() == None) and (node.getRight() == None):
            characterList[ord(node.getCharacter())] = inString
        else:
            self.charachterListEncodeHelper(characterList, node.getLeft(), inString + "0")
            self.charachterListEncodeHelper(characterList, node.getRight(), inString + "1")

    def createHeader(self, nodeList):
        header = ""
        for node in nodeList:
            header = header + str(ord(node.getCharacter())) + " " + str(node.getFrequency()) + " "
        header = header[:-1]
        return header

