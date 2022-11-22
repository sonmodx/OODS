class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, mT, mC) :
        self.maxTable = mT
        self.maxColli = mC
        self.hash = []
        for _ in range(0,self.maxTable) :
            self.hash.append(None)

    def keyASCII(self, data) :
        total = 0
        for item in data :
            total += ord(item)
        return total 

    def manageHash(self, data) :
        for i in range(0, len(data)) :
            indexOfTable = self.keyASCII(data[i].key)
            if self.hash[indexOfTable% self.maxTable] is None :
                self.hash[indexOfTable %self.maxTable] = data[i]
            else :
                indexOfTable = self.findNewIndex(indexOfTable, 0)
                if indexOfTable is not None :
                    self.hash[indexOfTable % self.maxTable] = data[i]
            self.printTable()
            if None not in self.hash :
                break
            
    def findNewIndex(self, indexOfTable, count) :
        if self.maxColli > count :
            index = (indexOfTable + (count*count)) 
            if self.hash[index % self.maxTable] is not None:
                print(f"collision number {count+1} at {index % self.maxTable}")
                return self.findNewIndex( indexOfTable, count+1)
            else :
                return index
        else :
            print("Max of collisionChain")
            return None

    def printTable(self) :
        for i in range(0, self.maxTable) :
            print(f"#{i+1}	{self.hash[i]}")
        print("---------------------------")

if __name__ =="__main__" :
    print(" ***** Fun with hashing *****")
    inp = input("Enter Input : ").split("/")
    ls = inp[1].split(',')
    data = []
    for item in ls :
        x = item.split()
        data.append(Data(x[0],x[1]))
    maxTable = int(inp[0].split()[0])       
    maxCollision = int(inp[0].split()[1])
    h = Hash(maxTable, maxCollision)
    h.manageHash(data)
    print("This table is full !!!!!!")