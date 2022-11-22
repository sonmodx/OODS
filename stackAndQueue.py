class Stack:
    def __init__(self,ls=None):
        if ls is None:
            self.ls  = []
        else:
            self.ls = ls
    
    def push(self,value):
        self.ls.append(value)

    def pop(self):
        return self.ls.pop()

    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def size(self):
        return len(self.ls)

    def __str__(self):
        return str(self.ls)

class Queue:
    def __init__(self,ls=None):
        if ls is None:
            self.ls  = []
        else:
            self.ls = ls
    
    def enqueue(self,value):
        self.ls.append(value)

    def dequeue(self):
        return self.ls.pop(0)

    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def size(self):
        return len(self.ls)

    def __str__(self):
        return str(self.ls)        

def findAlpha(s) :
    for letter in s:
        if letter.isalpha() :
            return True
    return False

if __name__ =="__main__":
    string = input().split(' ')
    ans = []
    print(string)
    last =0
    for inner in string :
        output = ""
        f = findAlpha(inner)
        if last ==0 and (inner =='+'or inner =='-'):
            ans.append(inner)
            continue

        if inner[-1].isalpha() and f:
            if len(inner) ==1:
                output+='1'
            output += inner[0:-1]
            last = 1
        elif f:
            
            output += str(int(inner[0:-3])*int(inner[-1]))
            output += inner[-3]
            if int(inner[-1])-1==1:
                ans.append(output)
                continue
            output += '^'
            output += str(int(inner[-1])-1)
        else :
            continue
        ans.append(output)

    print(' '.join(ans))
    