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
            else :
                node.left = Node(data)
        elif node.data < data :
            if node.right is not None:
                self.insert(data,node.right)
            else :
                node.right = Node(data)
        return node
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def moreThanK(self, data,node =None):
        if node is None:
            node = self.root
        if node.data > data :
            node.data = node.data * 3
        if node.left is not None:
            node.left = self.moreThanK(data, node.left)
        if node.right is not None:
            node.right = self.moreThanK(data, node.right)
        return node

        
            

if __name__ == '__main__':
    T = BST()
    sp = input('Enter Input : ').split('/')
    ls = [int(i) for i in sp[0].split()]
    k = int(sp[1])
    for i in ls:
        root = T.insert(i)
    T.printTree(root)
    print("--------------------------------------------------")
    T.moreThanK(k)
    T.printTree(root)