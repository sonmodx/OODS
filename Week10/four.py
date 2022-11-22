class Hash:
    def __init__(self, mT, mC, threshold) :
        self.maxTable = mT
        self.maxColli = mC
        self.threshold = threshold
        self.hash = []
        self.element = 0
        for _ in range(0,self.maxTable) :
            self.hash.append(None)

    def clearTable(self,maxTable) :
        count = 0
        for i in range(0,maxTable) :
            if self.hash[i] is not None :
                count += 1
            self.hash[i] = None
        return count
        

    def manageHash(self, data) :
        for i in range(0, len(data)) :
            print(f"Add : {data[i]}")
            if len(self.hash) * self.threshold / 100 < self.element + 1 :
                print("****** Data over threshold - Rehash !!! ******")
                self.scaleUpTable(len(self.hash))
                self.updateTable(data, i)

            indexOfTable = data[i]
            if self.hash[indexOfTable% self.maxTable] is None :
                self.hash[indexOfTable %self.maxTable] = data[i]
                self.element += 1
            else :
                indexOfTable = self.findNewIndex(indexOfTable, 0,data ,i)
                
                self.hash[indexOfTable % self.maxTable] = data[i]
                self.element += 1
            self.printTable()
            if None not in self.hash :
                break
            
    def findNewIndex(self, indexOfTable, count,data , i) :
        if self.maxColli > count :
            index = (indexOfTable + (count*count)) 
            if self.hash[index % self.maxTable] is not None:
                print(f"collision number {count+1} at {index % self.maxTable}")
                return self.findNewIndex( indexOfTable, count+1,data,i)
            else :
                return index
        else :
            print("****** Max collision - Rehash !!! ******")
            self.scaleUpTable(len(self.hash))
            self.updateTable(data,i)
            return self.findNewIndex( indexOfTable, 0,data,i)

    def updateTable(self, data, r) :
        for i in range(0, r) :
            indexOfTable = data[i]
            if self.hash[indexOfTable% self.maxTable] is None :
                self.hash[indexOfTable %self.maxTable] = data[i]
            else :
                indexOfTable = self.findNewIndex(indexOfTable, 0,data,i)
                
                self.hash[indexOfTable % self.maxTable] = data[i]

    def scaleUpTable(self,maxTable) :
        self.clearTable(maxTable)
        number = self.nextPrimeNumber()
        extenses = number - len(self.hash)  
        for _ in range(0,extenses) :
            self.hash.append(None)
        self.maxTable = len(self.hash)
        

    def nextPrimeNumber(self) :
        def isPrime(number) :
            if number <= 1 :
                return False
            for i in range(2,number//2) :
                if number % i == 0:
                    return False
            return True
        start = len(self.hash) * 2 + 1
        while True :
            if isPrime(start) :
                return start
            start = start + 1

    def printTable(self) :
        for i in range(0, self.maxTable) :
            print(f"#{i+1}	{self.hash[i]}")
        print("----------------------------------------")

if __name__ =="__main__" :
    print(" ***** Rehashing *****")
    inp = input("Enter Input : ").split("/")
    ls = [int(x) for x in inp[1].split()]
    maxTable = int(inp[0].split()[0])       
    maxCollision = int(inp[0].split()[1])
    threshold = int(inp[0].split()[2])
    h = Hash(maxTable, maxCollision, threshold)
     ##init table
    print("Initial Table :")
    h.printTable()
    h.manageHash(ls)