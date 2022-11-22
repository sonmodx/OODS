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

    def insert(self, val, node, output=""):
        if self.root is None :
            print("*")
            return Node(val)
        elif node.data > val :
            output += "L"
            if node.left is not None: 
                self.insert(val,node.left,output)
            else :
                node.left = Node(val)
                print(output+"*")
        elif node.data < val :
            output += "R"
            if node.right is not None:
                self.insert(val,node.right,output)
            else :
                node.right = Node(val)
                print(output+"*")
        return node

if __name__ == '__main__':
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        T.root = T.insert(i, T.root)
    