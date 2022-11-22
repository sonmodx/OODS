class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None
    
    def appendFirst(self,value):
        node = Node(value,self.head)
        self.head = node

    def appendLast(self,value):
        if self.head is None:
            self.appendFirst(value)
            return
        itr = self.head
        while itr.next:
            itr= itr.next
        itr.next = Node(value,None)
        return
    
    def size(self):
        count =0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count

    def insertAt(self,index,value):
        if index < 0 or index > self.size():
            raise Exception("Invalide index")
        if index==0:
            self.appendFirst(value)
            return
        count =0
        itr = self.head
        while itr:
            if count==index-1:
                itr.next = Node(value,itr.next)
                break
            itr = itr.next
            count+=1
    
    def removeAt(self,index):
        if index <0 or index >self.size():
            raise Exception("Invalide index")

        if index ==0 :
            self.head = self.head.next
            return
        
        itr = self.head
        count =0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def printList(self):
        if self.head is None :
            print("Linklist is empty!")
            return
        itr = self.head
        output = ""
        while itr:
            output += (str(itr.value))
            if itr.next is not None:
                output += (" ")
            itr = itr.next
        
        return output

def merge(l1,l2) :
    itr = l1.head
    while itr.next:
        itr = itr.next
    itr.next = l2.head
    return l1

if __name__ =="__main__":
    l1,l2 = input("Enter Input (L1,L2) : ").split(' ')
    l1 = l1.split('->')
    l2 = l2.split('->')
    L1 = LinkList()
    L2 = LinkList()
    for a in l1 :
        L1.appendLast(a)
    for a in l2 :
        L2.appendFirst(a)
    print("L1    : ",end="")
    print(L1.printList())
    print("L2    : ",end="")
    print(' '.join(list(reversed((L2.printList().split(' '))))))
    print("Merge : ",end="")
    a =  merge(L1,L2)
    print(a.printList())
