
class BST:
    def __init__(self,value,left=None,right=None) :
        self.value = value
        self.left = left
        self.right = right
    
    def add_child(self,value) :
        if self.value == value :
            return
        if self.value > value :
            if self.left:
                self.left.add_child(value)
            else :
                self.left = BST(value)
        elif self.value < value :
            if self.right:
                self.right.add_child(value)
            else :
                self.right = BST(value)

    def inorder_traversed(self) :
        ls = []
        #lnr
        if self.left :
            ls += self.left.inorder_traversed()
        ls.append(self.value)
        if self.right :
            ls += self.right.inorder_traversed()
        return ls

    def search(self,value) :
        if self.value == value:
            return True
        if self.value > value:
            if self.left :
                return self.left.search(value)
            else :
                return False
        elif self.value < value:
            if self.right :
                return self.right.search(value)
            else :
                return False

    def find_max(self) :
        if self.right :
            return self.right.find_max()
        return self.value

    def find_min(self) :
        if self.left :
            return self.left.find_min()
        return self.value

    def cal_sum(self) :
        left_side = self.left.cal_sum() if self.left else 0
        right_side = self.right.cal_sum() if self.right else 0
        return left_side + right_side + self.value

    def delete(self,value) :
        if self.value > value:
            if self.left :
                self.left = self.left.delete(value)
        elif self.value < value:
            if self.right :
                self.right = self.right.delete(value)
            
        else :
            if self.left is None and self.right is None :
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_value = self.right.find_min()
            self.value = min_value
            self.right = self.right.delete(min_value)
        return self
        

def buildTree(element) :
    root = BST(element[0])
    for ele in element[1:] :
        root.add_child(ele)
    return root


if __name__ == '__main__':
    tree = buildTree([1,2,3,-1])
    print(tree.inorder_traversed())
    print(tree.find_min())
    print(tree.cal_sum())
    tree.delete(-1)
    print(tree.inorder_traversed())