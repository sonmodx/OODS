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
    
    def removeHead(self):
        number = self.head.value
        self.head=self.head.next
        return number

    def peek(self):
        return self.head.value

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
                output+=" -> "
            itr = itr.next
        return output

def max_digit(n):
    c=0
    
    while n>0:
        n//=10
        c+=1
    return c

def get_digit(n,d):
    for _ in range(d-1):
        n//=10
    return n%10

def sort(ll):
    oneLineOnZero = 1
    for i in range(10):
        if i!=0 and ll[i].size()!=0 :
            oneLineOnZero = 0
        if ll[i].size()!=0:
            #so sort
            j=0
            while j<ll[i].size():
                k=0
                itr = ll[i].head
                while k <ll[i].size()-j and itr.next:
                    if itr.value > itr.next.value:
                        itr.value,itr.next.value = itr.next.value,itr.value
                    itr = itr.next
                    k+=1
                j+=1
    return oneLineOnZero
    

if __name__ == "__main__":
    data = [int(a) for a in input("Enter Input : ").split()]
    print("------------------------------------------------------------")
    before,store = LinkList(),LinkList()
    for d in data:
        before.appendLast(d)
        store.appendLast(d)
    
    ll = [LinkList(),LinkList(),LinkList(),LinkList(),LinkList(),LinkList(),LinkList(),LinkList(),LinkList(),LinkList()]
    times = 0
    for i in range(1,max_digit(max([int(abs(a)) for a in data]))+2) :
        print("Round : "+str(i))
        while store.size()!=0:
            number = int(store.removeHead())
            if number<0:
                digit = get_digit(number*-1,i)
                ll[digit].appendLast(number)
            else :
                digit = get_digit(number,i)
                ll[digit].appendLast(number)
        #check!!
        oneLineOnZero =  sort(ll)
        for i in range(10):
            print(str(i)+" : ",end="")
            while ll[i].size()!=0:
                print(ll[i].peek(),end=" ")
                store.appendLast(ll[i].removeHead())
                
            print("")
        print("------------------------------------------------------------")
        times+=1
        if oneLineOnZero ==1 :
            break
    print(f"{times-1} Time(s)")
    print("Before Radix Sort : "+before.printList())
    print("After  Radix Sort : "+store.printList())

