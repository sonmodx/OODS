class Node :
    def __init__(self,val,prev=None,next=None) :
        self.val = val
        self.prev= prev
        self.next = next

class DoublyLinklist :
    def __init__(self) :
        self.head = None
        self.tail = None

    def addHead(self,val) :
        node = Node(val)
        node.next = self.head
        if self.head is not None :
            self.head.prev = node
        self.head  = node
        last = self.head
        while last.next:
            last = last.next
        self.tail = last
        self.tail.prev = last.prev

    def append(self,val) :
        node = Node(val)
        if self.head is None :
            self.addHead(val)
            return
        last = self.head
        while last.next:
            last=  last.next
        last.next = node
        self.tail = node
        self.tail.prev = last 

    def size(self) :
        count = 0
        itr = self.head
        while itr :
            itr = itr.next
            count += 1
        return count

    def insertAt(self,pos,val) :
        if pos == 0 or (pos < 0 and pos *-1 > self.size()) :
            self.addHead(val)
            return
        if pos > self.size() :
            self.append(val)
            return
        if pos < 0 :
            pos *=-1
            pos = self.size() - pos
        itr = self.head
        count =0
        while itr.next :
            self.tail = itr.next
            if count == pos-1 :
                itr.next = Node(val,itr,itr.next)
                self.tail.prev = itr.next
            itr = itr.next
            count += 1
        return

    def pop(self,pos) :
        if pos < 0 or pos >=self.size():
            return "Empty"
        if self.head is None :
            return " Empty"
        if pos == 0:
            self.head = self.head.next
            self.head.prev = None
        itr = self.head
        count =0
        while itr :
            #last element
            if pos == self.size()-1 :
                self.tail = self.tail.prev
                
            #middle element
            elif count == pos-1:
                itr.next = itr.next.next
                
            elif count == pos:
                itr.prev = itr.prev.prev
            itr = itr.next
            count += 1
        return
        
    def __str__(self) :
        output = ""
        itr  = self.head
        while itr :
            output += str(itr.val)
            if itr.next is not None :
                output += " "
            itr = itr.next
        return output

    def reverse(self) :
        output = ""
        itr  = self.tail
        while itr :
            output += str(itr.val)
            if itr.prev is not None :
                output += " "
            itr = itr.prev
        return output
        
if __name__ == '__main__' :
    dll = DoublyLinklist()
    dll.append(4)
    dll.append(10)
    dll.append
    print(dll)
    print(dll.reverse())
