class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.previous = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        node = Node(item)
        last = self.head
        self.tail = node

        if self.head is None:
            self.head = node
            return
        
        while last.next :
            last = last.next
        last.next = node
        self.tail.previous = last
        return

    def addHead(self, item):
        node = Node(item)
        node.next = self.head

        if self.head is not None:
            self.head.previous = node
        self.head = node
        last = self.head

        while last.next:
            last= last.next
            
        self.tail = last
        self.tail.previous = last.previous
        return

    def insert(self, pos, item):
        if pos==0 or (pos < 0 and pos *-1>self.size()):
            self.addHead(item)
            return
        if pos > self.size():
            self.append(item)
            return
        count =0
        itr = self.head
        
        if pos<0 :
            pos *=-1
            pos = self.size()-pos
        while itr.next:
            self.tail = itr.next
            if count== pos-1:
                itr.next = Node(item,itr,itr.next)
                self.tail.previous = itr.next
                
            itr = itr.next
            count+=1
        return
       
    def search(self, item):
        itr = self.head
        while itr:
            if itr.value==item:
                return "Found"
            itr = itr.next
        return "Not Found"

    def index(self, item):
        if self.search(item)=="Not Found":
            return "-1"
        itr = self.head
        count =0
        while itr:
            if itr.value==item:
                return str(count) 
            itr = itr.next
            count += 1
        

    def size(self):
        count =0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count

    def pop(self, pos): 
        if self.size()==0:
            return "Out of Range"
        if pos < 0 or pos >= self.size():
            return "Out of Range"
        if pos ==0 :
            #delete at head
            self.head = self.head.next
            self.head.previous = None
            return "Success"
        
        count =0 
        itr = self.head
        
        while itr:
            #delete at tail
            if pos == self.size()-1 and count==pos-1:
                itr.next = None
                self.tail = self.tail.previous 
            #delete between
            elif count == pos -1 :
                itr.next = itr.next.next
            elif count == pos:
                itr.previous = itr.previous.previous

            
            itr =itr.next
            count += 1
        return "Success"
        

dll = LinkedList()


print(dll)
    
print(dll.reverse())
# L = LinkedList()
# inp = input('Enter Input : ').split(',')
# for i in inp:
#     if i[:2] == "AP":
#         L.append(i[3:])
#     elif i[:2] == "AH":
#         L.addHead(i[3:])
#     elif i[:2] == "SE":
#         print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
#     elif i[:2] == "SI":
#         print("Linked List size = {0} : {1}".format(L.size(), L))
#     elif i[:2] == "ID":
#         print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
#     elif i[:2] == "PO":
#         before = "{}".format(L)
#         k = L.pop(int(i[3:]))
#         print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
#     elif i[:2] == "IS":
#         data = i[3:].split()
#         L.insert(int(data[0]), data[1])
# print("Linked List :", L)
# print("Linked List Reverse :", L.reverse())