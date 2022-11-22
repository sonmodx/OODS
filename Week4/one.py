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
        return self.ls.pop(0) + " 0"

    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def sizeQueue(self):
        return len(self.ls)

    def __str__(self):
        if self.ls ==[]:
            return "Empty"
        return str(self.ls)[1:-1].replace(', ',' ').replace('\'','')  

if __name__ == "__main__":
    s = input("Enter Input : ").split(',')
    q = Queue()
    for i in s:
        if 'E' in i:
            print(q.enqueue(i[2:]))
        else:
            print(q.dequeue())
    print(q)
