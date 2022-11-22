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

    def checkpos(self, data,node = None):
        # Root: node = self.root and node.left is not None and node.right is not None 
        # inner: node != self.root and (node.left is not None or node.right is not None) 
        # leaf: else ... 
        if node is None :
            node = self.root
        if node.data > data :
            if node.left is not None :
                return self.checkpos(data,node.left)
        elif node.data < data :
            if node.right is not None :
                return self.checkpos(data,node.right)
        else :
            if node == self.root :
                return "Root"
            if node != self.root and (node.left is not None or node.right is not None):
                return "Inner"
            if node != self.root and node.left is None and node.right is None:
                return "Leaf"
            return None
            
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == '__main__':
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in range(1, len(inp)):
        root = T.insert(inp[i])
    T.printTree(root)
    pos = T.checkpos(inp[0])
    print("Not exist" if pos == None else pos)