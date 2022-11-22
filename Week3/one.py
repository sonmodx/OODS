class Stack:
    def __init__(self,ls=None):
        if ls is None:
            self.ls  = []
        else:
            self.ls = ls
        self.size = 0
    
    def push(self,value):
        self.ls.append(value)
        if self.size<0:
            self.size =0
        self.size += 1
        print(f"Add = {value} and Size = {self.size}")

    def pop(self):
        if self.isEmpty() :
            print("-1")
            return -1
        self.size -= 1
        
        print(f"Pop = {str(self.ls.pop())} and Index = {self.size}")

    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def size(self):
        return self.size

    def __str__(self):
        if self.ls == []:
            return "Empty"
        return str(self.ls)[1:-1].replace(', ',' ').replace('\'','')

if __name__ =="__main__":
    l = []
    for s in input("Enter Input : ").split(',') :
        if 'A' in s :
            l.append(s[2:])
        else :
            l.append(s)
    s = Stack()
    for i in l :
        if i.isdigit():
            s.push(i)
        else :
            s.pop()
    print(f"Value in Stack = {s}") 