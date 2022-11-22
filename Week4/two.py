class Queue:
    def __init__(self,ls=None):
        if ls is None:
            self.ls  = []
        else:
            self.ls = ls
        self.size =0
    
    def enqueue(self,value):
        self.ls.append(value)
        self.size +=1
        return self.size

    def dequeue(self):
        if self.size==0:
            return -1
        self.size-=1
        return self.ls.pop(0)

    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def sizeQueue(self):
        return len(self.ls)

    def __str__(self):
        return str(self.ls)

if __name__ == "__main__":
    mainQ = Queue()
    firstQ = Queue()
    secondQ = Queue()
    string = input("Enter people : ")
    for letter in string :
        mainQ.enqueue(letter)
    
    for i in range(1,len(string)+1) :
        if (i-1)%3==0 and not firstQ.isEmpty():
            firstQ.dequeue()
        if i%2==0 and not secondQ.isEmpty():
            secondQ.dequeue()
        if firstQ.sizeQueue()==5:
            secondQ.enqueue(mainQ.dequeue())
        else:    
            firstQ.enqueue(mainQ.dequeue())
        print(f"{i} {mainQ} {firstQ} {secondQ}")

