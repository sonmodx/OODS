class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None 

    def insert(self, data, node=None):
        if node is None :
            node = self.root
        if self.root is None :
            self.root = Node(data)
            
        elif node.data > data :
            if node.left is not None: 
                self.insert(data,node.left)
                # self.insert(data)
                #node.left.insert(data)
            else :
                node.left = Node(data)
        elif node.data < data :
            if node.right is not None:
                self.insert(data,node.right)
                # self.insert(data)
                #node.right.insert(data)
            else :
                node.right = Node(data)
        return node
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == '__main__':
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = T.insert(i)
    T.printTree(root)