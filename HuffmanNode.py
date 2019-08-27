class Node:
    #Class representing Huffman Node to be used in the compression process.

    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        if character == None:
            self.minimum = None
        else:
            self.minimum = ord(character)
        self.left = None
        self.right = None

    def __str__(self):
        return "HuffmanNode"

    #Getter Functions/Accessor Methods.
    def getCharacter(self):
        return self.character

    def getFrequency(self):
        return self.frequency

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getMinimum(self):
        return self.minimum

    #Setter Functions/Mutator Methods.
    def setCharacter(self, character):
        self.character = character

    def setFrequency(self, frequency):
        self.frequency = frequency

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setMinimum(self, minimum):
        self.minimum = minimum
