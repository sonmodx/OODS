class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val, node=None):
        if node is None :
            node = self.root
        if self.root is None :
            self.root = Node(val)
            node = self.root
        
        elif node.data > val :
            if node.left is not None: 
                self.insert(val,node.left)
            else :
                node.left = Node(val)
        elif node.data < val :
            if node.right is not None:
                self.insert(val,node.right)
            else :
                node.right = Node(val)
        return node

    def search(self,value,node =None) :
        if node is None:
            node = self.root
        if node.data == value:
            return True
        if node.data > value:
            if node.left :
                return self.search(value,node.left)
            else :
                return False
        elif node.data < value:
            if node.right :
                return self.search(value,node.right)
            else :
                return False

    def find_min(self, node=None) :
        if node is None:
            node = self.root
        if node.left is not None:
            return self.find_min(node.left)
        return node.data

    def delete(self, data, node=None):
        if self.root is None or self.search(data,node) is False:
            print("Error! Not Found DATA")
            return self.root
        if node is None:
            node = self.root
        if node.data > data:

            node.left = self.delete(data,node.left)
        elif node.data < data:

            node.right = self.delete(data,node.right)
        else:
            if node.left is not None and node.right is not None:

                min_value = self.find_min(node.right)
                node.data = min_value
                node.right = self.delete(min_value,node.right)
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else :
                if self.root.left is None and self.root.right is None:
                    self.root = None
                return None   
        return node
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

if __name__ == '__main__':
    tree = BinarySearchTree()
    data = input("Enter Input : ").split(",")
    for d in data :
        if d[0]=='i':
            print(f"insert {d[2:]}")
            tree.root = tree.insert(int(d[2:]))
            printTree90(tree.root)
        else :
            print(f"delete {d[2:]}")
            tree.root = tree.delete(int(d[2:]))
            printTree90(tree.root)
        