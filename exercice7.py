class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

    def insert(self, dataToInsert):
        if dataToInsert <= self.data:
            if self.left is None:
                self.left = Node(dataToInsert)
                self.left.parent = self
            else:
                self.left.insert(dataToInsert)
        elif dataToInsert > self.data:
            if self.right is None:
                self.right = Node(dataToInsert)
                self.right.parent = self
            else:
                self.right.insert(dataToInsert)

    def pprint(self, level=0):
        if self.right:
            self.right.pprint(level + 1)
        print(f"{' ' * 4 * level}{self.data}")
        if self.left:
            self.left.pprint(level + 1)

nodesNumber = int
root = int
root = (int(input("Veuillez indiquer la valeur de la racine de l'arbre : ")))
nodesNumber = (int(input("Veuillez maintenant indiquer le nombre de noeuds dans l'arbre : ")))


bst = Node(root)
i = 0
while i < nodesNumber:
    nodeValue = int(input("Veuillez entrer une valeur : "))
    bst.insert(nodeValue)
    i += 1

bst.pprint()