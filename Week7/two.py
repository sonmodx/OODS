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

    def inorderBelow(self, data,node):
        elements = []
        # if node is None :
        #     node = self.root
        #lnr
        if node.left is not None:
            elements += self.inorderBelow(data,node.left)
        if node.data < data:
            elements.append(node.data)
        if node.right is not None:
            elements += self.inorderBelow(data,node.right)
        return elements
            

if __name__ == '__main__':
    
    T = BST()
    sp = input('Enter Input : ').split('|')
    ls = [int(i) for i in sp[0].split()]
    lowerNumber = int(sp[1])
    for i in ls:
        root = T.insert(i)
    T.printTree(root)
    print("--------------------------------------------------")
    res = T.inorderBelow(lowerNumber,T.root)
    print(f"Below {lowerNumber} :",end=" ")
    print(str(res)[1:-1].replace(',','')) if res !=[] else print("Not have")