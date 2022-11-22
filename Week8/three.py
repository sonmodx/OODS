class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.rank = 1
    def __str__(self):
        return str(self.data) 

class BST:
    def __init__(self): 
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
        elif node.data < val :
            if node.right is not None:
                node.right = self.insert(val,node.right)
            else :
                node.right = Node(val)
        
        return node

    def find_min(self, node=None) :
        if node is None:
            node = self.root
        if node.left is not None:
            return self.find_min(node.left)
        return node.data

    def find_max(self, node=None) :
        if node is None:
            node = self.root
        if node.right is not None:
            return self.find_max(node.right)
        return node.data

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def findRank(find_val, node) :
    if node is None :
        return 0
    if find_val >= node.data :
        return 1 + findRank(find_val, node.left) + findRank(find_val, node.right)
    else :
        return findRank(find_val, node.left)
            
       
if __name__ =='__main__' :
    tree = BST()
    inp = input("Enter Input : ").split('/')
    item = [int(a) for a in inp[0].split()]
    find_value = int(inp[1])
    for i in item :
        tree.root = tree.insert(i,tree.root)
    tree.printTree(tree.root)
    print("--------------------------------------------------")
    rank = 0
    if find_value < tree.find_min(tree.root) :
        rank = 0
    elif find_value > tree.find_max(tree.root) :
        rank = len(item)
    else :
        rank = findRank(find_value, tree.root)
    print(f"Rank of {find_value} : {rank}")

