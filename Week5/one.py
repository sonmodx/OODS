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
        output = ''
        while itr:
            output += str(itr.value)
            if itr.next is not None:
                output+=" <- "
            itr = itr.next
        print(output)

    def afterZero(self,ll):
        itr = ll.head
        while itr.value != 0:
            itr = itr.next
        self.head = itr 
        

    def beforeZero(self,ll):
        itr = self.head
        while itr.next:
            itr = itr.next
        temp = ll.head
        while temp.value!=0:
            itr.next = Node(temp.value,itr.next)
            itr = itr.next
            temp = temp.next


if __name__ == "__main__":
    print(" *** Locomotive ***")
    listString = [int(a) for a in input("Enter Input : ").split(' ')]
    ll = LinkList()
    newLl = LinkList()
    for a in listString :
        ll.appendLast(a)
    
    print("Before : ",end="")
    ll.printList()
    print("After : ",end="")    
    newLl.afterZero(ll)
    newLl.beforeZero(ll)
    newLl.printList()
    