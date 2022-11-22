output = "No Loop"
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
            print("Empty")
            return
        itr = self.head
        output = ''
        while itr:
            output += str(itr.value)
            if itr.next is not None:
                output+="->"
            itr = itr.next
        print(output)

    def changeNext(self,string):
        first,second = string.split(':')
        first = int(first)
        second = int(second)
        if self.size()==0 :
            return "Error! {list is empty}"
        if first >= self.size() or first < 0:
            return "Error! {index not in length}: " + str(first)
        if second >= self.size() or second < 0:
            self.appendLast(second)
            return "index not in length, append : " + str(second)
        
        #Loop
        if first>= second :
            global output
            output = "Found Loop"
            itr =self.head
            count =0
            while count!=second :
                itr = itr.next
                count += 1
            temp = itr
            numSec = temp.value
            numFirst = numSec
            while itr:
                if count ==first-1:
                    numFirst = itr.next.value
                    break
                itr = itr.next
                count+=1
            out = f"Set node.next complete!, index:value = {first}:{numFirst} -> {second}:{numSec}"
            return out
        #No Loop
        number = 0
        itr = self.head
        
        while number != first:
            itr = itr.next
            number+=1
        #print(itr.value)
        temp = itr
        numFirst = temp.value
        numSec = 0
        while itr:
            if number == second-1:
                numSec = itr.next.value
                temp.next = itr.next
                break
            itr = itr.next
            number+=1
        out = f"Set node.next complete!, index:value = {first}:{numFirst} -> {second}:{numSec}"
        return out
         
        
if __name__=="__main__":
    stringList = input("Enter input : ").split(',')
    ll = LinkList()
    for a in stringList :
        if a[0] == 'A':
            ll.appendLast(a[2:])
            ll.printList()
        else :
            print(ll.changeNext(a[2:]))
    print(output)
    if output == "No Loop" :
        ll.printList()