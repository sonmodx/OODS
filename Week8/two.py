class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self) :
        self.root = None

    def insert(self, val, node):
        if self.root is None :
            self.root = Node(val)
            node = self.root
        elif node.data > val :
            if node.left is not None: 
                node.left = self.insert(val,node.left)
            else :
                node.left = Node(val)
        elif node.data <= val :
            if node.right is not None:
                node.right = self.insert(val,node.right)
            else :
                node.right = Node(val)
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))

        balance = self.getBalance(node)

        
        if balance > 1 and val >= node.left.data:
            node = self.RightLeftRotate(node)

        elif balance > 1 and val <= node.left.data:
            node = self.rightRotate(node)

        elif balance < -1 and val < node.right.data:
            node = self.LeftRightRotate(node)

        elif balance < -1 and val >= node.right.data:
            node = self.leftRotate(node)
        return node
 
    def rightRotate(self, px):
        py = px.left
        px.left = py.right
        py.right = px
        px.height = 1 + max(self.getHeight(px.left),self.getHeight(px.right))
        py.height = 1 + max(self.getHeight(py.left),self.getHeight(py.right))
        return py

    def leftRotate(self, px):
        py = px.right
        px.right = py.left
        py.left = px
        px.height = 1 + max(self.getHeight(px.left),self.getHeight(px.right))
        py.height = 1 + max(self.getHeight(py.left),self.getHeight(py.right))
        return py

    def RightLeftRotate(self, px):
        py = px.left
        px.left = self.leftRotate(py)
        px = self.rightRotate(px)
        return px

    def LeftRightRotate(self, px):
        py = px.right
        px.right = self.rightRotate(py)
        px = self.leftRotate(px)
        return px

    def getHeight(self,node):
        if node is None :
            return 0
        return node.height

    def getBalance(self,node):
        if node is None :
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == '__main__' :
    inp = [int(i) for i in input('Enter Input : ').split()]
    tree = AVL()
    for i in inp:
        tree.root = tree.insert(i, tree.root)
        print(f"Insert : ( {i} )")
        tree.printTree(tree.root)
        print("--------------------------------------------------")
        
