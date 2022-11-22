class Heap :
    def __init__(self) :
        self.heap = []
        self.element = 0

    def insert(self, item, numberVan) :
        if self.element >= len(self.heap) :
            self.heap.append([item, numberVan])
            self.element = self.element + 1
            self.percolateUp(len(self.heap) - 1)
        else :
            self.heap[self.element] = [item,numberVan]
            self.element = self.element + 1
            self.percolateUp(self.element - 1)

    def getMin(self) :
        if self.element <= 0:
            return None
        return self.heap[0]

    def removeMin(self) :
        minimum = self.heap[0]
        if self.element == 0 :
            return None
        if self.element == 1 :
            self.element = self.element - 1
            return minimum
        else : 
            self.heap[0] = self.heap[self.element - 1]
            self.element = self.element - 1
            self.heapify(0)
            return minimum


    def percolateUp(self,index) :
        #from child to parent
        if index <= 0 :
            return 
        parent = ( (index - 1 )// 2)
        if self.heap[parent][0] > self.heap[index][0] or (self.heap[parent][0] == self.heap[index][0] and self.heap[parent][1] > self.heap[index][1]):
            #swap
            self.heap[parent] , self.heap[index] = self.heap[index], self.heap[parent]
            self.percolateUp(parent)

    def size(self) :
        return self.element

    def heapify(self,index) :
        #from root to last child
        left = (index*2) + 1
        right = (index*2) + 2
        current = index
        if (self.element > left and self.heap[current][0] > self.heap[left][0]) or (self.element > left and self.heap[current][0] == self.heap[left][0] and self.heap[current][1] > self.heap[left][1]):
            current = left
            
        if (self.element > right and self.heap[current][0] > self.heap[right][0]) or (self.element > right and self.heap[current][0] == self.heap[right][0] and self.heap[current][1] > self.heap[right][1]):
            current = right
        
        if current != index :
            self.heap[current] , self.heap[index] = self.heap[index], self.heap[current]
            self.heapify(current)

    def buildMinHeap(self,ls,k) :
        for numberVan in range(0,k) :
            if numberVan < len(ls) :
                self.insert(ls[numberVan], numberVan+1) 
            else :
                break

    def decreaseDay(self) :
        for i in range(0,self.element) :
            self.heap[i][0] = self.heap[i][0] - 1


def manageVans(heap,k,ls) :
    van = 1
    m = k
    for i in range(0, len(ls)) :
        if i < k: 
            print(f"Customer {i+1} Booking Van {van} | {ls[i]} day(s)")
            van = (van % m ) + 1
        else :
            van = heap.removeMin()
            print(f"Customer {i+1} Booking Van {van[1]} | {ls[i]} day(s)")
            heap.decreaseDay()
            heap.insert(ls[i],van[1])
    return

if __name__ =='__main__' :
    k ,ls = input("Enter Input : ").split('/')
    ls ,k= [int(a) for a in ls.split()] ,int(k)
    temp = ls[::]
    myHeap = Heap()
    myHeap.buildMinHeap(ls,k)
    manageVans(myHeap,k,temp)