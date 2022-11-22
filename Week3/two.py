class Stack:
    def __init__(self,ls=None):
        if ls is None:
            self.ls  = []
        else:
            self.ls = ls
        self.size =0
    
    def push(self,value):
        self.ls.append(value)
        self.size +=1

    def pop(self):
        if self.isEmpty() :
            print("-1")
            return -1
        self.size -= 1
        
        print(f"Pop = {str(self.ls.pop())}")


    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def size(self):
        return len(self.ls)

    def deleteValue(self,value):
        if not self.isEmpty():
            for i in reversed(range(0,self.size)) :
                if self.ls[i] == value:
                    print(f"Delete = {value}")
                    self.ls.pop(i)
                    self.size -=1
                    
                    
        else :
            print("-1")
        return

    def deleteValueLessthan(self,value):
        if not self.isEmpty():
            for i in reversed(range(0,self.size)) :
                if int(self.ls[i]) < int(value):
                    
                    print(f"Delete = {self.ls[i]} Because {self.ls[i]} is less than {value}")
                    self.ls.pop(i)
                    
                    
                    self.size -=1
                    
        else :
            print("-1")
        return

    def deleteValueMorethan(self,value):
        if not self.isEmpty():
            for i in reversed(range(0,self.size)) :
                if self.ls[i] > value:
                    print(f"Delete = {self.ls[i]} Because {self.ls[i]} is more than {value}")
                    self.ls.pop(i)
                    
                    
                    self.size -=1
                       
        else :
            print("-1")
        return

    def ManageStack(self,s,value=None) :
        if s=="A":
            self.push(value)
            print(f"Add = {value}")
            return
        if s=="P":
            self.pop()
            return
        if s=="D":
            self.deleteValue(value)
            return
        if s=="LD":
            self.deleteValueLessthan(value)
            return
        if s=="MD":
            self.deleteValueMorethan(value)
            return

    def __str__(self):
        return str(self.ls)


if __name__ =="__main__":
    l = []
    for s in input("Enter Input : ").split(',') :
        l.append(s)
    s = Stack()
    for i in l :
        if 'A' in i:
            s.ManageStack("A",i[2:])
        elif 'P' in i:
            s.ManageStack("P")
        elif 'D' in i and 'LD' not in i and 'MD' not in i:
            s.ManageStack("D",i[2:])
        elif 'LD' in i:
            s.ManageStack("LD",i[3:])
        elif 'MD' in i:
            s.ManageStack("MD",i[3:])
    output = str(s).replace('\'','')
    print(f"Value in Stack = {output}")
    
