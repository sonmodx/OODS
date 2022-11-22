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
        self.size-=1
        return self.ls.pop()
        

    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def sizeStack(self):
        return self.size


    def findThreeLetter(self):
        temp = []
        combo=0
        for letter in self.ls :
            temp.append(letter)
            if len(temp)>=3:
                if self.checkThree(temp) :
                    combo+=1
                    for i in range(0,3) :
                        temp.pop()
            
        return temp,len(temp),combo

    def checkThree(self,stack) :
        count =0
        for i in range(0,len(stack)-2) :
            if stack[i] == stack[i+1] and stack[i+1] == stack[i+2]:
                count =1
            else :
                count =0
            if count==1 :
                return True
        return False
        


    def __str__(self):
        return str(self.ls)


if __name__ == "__main__":
    inp = input('Enter Input : ').split()

    S = Stack()
    for l in inp :
        S.push(l)

    temp,lengthOfTemp,combo = S.findThreeLetter()
    print(lengthOfTemp)
    
    if temp==[] :
        print("Empty")
    else :
        print(str(temp)[1:-1].replace(', ','').replace('\'','')[::-1])
         
    if combo>1:
        print(f"Combo : {combo} ! ! !")
