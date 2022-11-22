class Stack:
    def __init__(self,ls=None):
        if ls is None:
            self.ls  = []
        else:
            self.ls = ls
        self.size=0
    
    def push(self,value):
        self.ls.append(value)
        self.size+=1

    def pop(self):
        self.size-=1
        return self.ls.pop()

    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def sizeStack(self):
        return len(self.ls)

    def countBack(self):
        mx=0
        temp = Stack()
        if self.isEmpty() :
            return 0

        for i in reversed(range(0,self.sizeStack())) :
            if int(self.ls[i])>int(mx):
                mx = int(self.ls[i])
                temp.push(self.ls[i])
        return temp.sizeStack()

    def __str__(self):
        return str(self.ls)


if __name__ =="__main__":
    l = []
    for x in input("Enter Input : ").split(',') :
        if 'A' in x :
            l.append(x[2:])
        else :
            l.append(x)
    s = Stack()
    for i in l :
        if i.isdigit():
            s.push(i)
        else :
            print(str(s.countBack()))
            
