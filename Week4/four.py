class Queue:
    def __init__(self,ls=None):
        if ls is None:
            self.ls  = []
            self.size =0
        else:
            self.ls = list(ls)
            self.size=len(self.ls)
    
    def enqueue(self,value):
        self.ls.append(value)
        self.size+=1

    def dequeue(self):
        if self.size==0:
            return -1
        self.size-=1
        return self.ls.pop(0)

    def peek(self):
        return self.ls[0]

    def isEmpty(self):
        return self.ls == []

    def sizeQueue(self):
        return len(self.ls)

    def __str__(self):
        return str(self.ls)

def checkQueue(l):
    match = Queue()
    total=0
    for i in l :
        count =0
        findFirstColon = i.index(':')
        findSecondColon = i.index(':',2)

        match.enqueue(i[findFirstColon-1])
        match.enqueue(i[findSecondColon-1])
        if match.dequeue() == match.dequeue() :
            count +=1
        
        match.enqueue(i[findFirstColon+1])
        match.enqueue(i[findSecondColon+1])
        if match.dequeue() == match.dequeue() :
            count +=2
        if count ==3 :
            count = 4
        elif count ==0 :
            count -=5
        total += count
    return total
        
def translateNumberToWord(q):
    output = ""
    act = { "0" : "Eat",
            "1" : "Game",
            "2" : "Learn",
            "3" : "Movie"}

    place = {"0": "Res.",
             "1": "ClassR.",
             "2": "SuperM.",
             "3": "Home"}
    colon =0
    for i in range(len(q)):
        if q[i].isdigit():
            number = q[i]
            if colon==0 :     
                output += act[str(number)]
            else :
                output += place[str(number)]
                colon =0
        elif q[i]==':' :
            colon= 1
            output += q[i]
        else :
            output += q[i]
    return output

if __name__ == "__main__":
    l = input("Enter Input : ").split(',')
    myQueue = [a.split(' ')[0] for a in l]
    yourQueue = [a.split(' ')[1] for a in l]
    myQ = ', '.join(myQueue)
    yourQ = ', '.join(yourQueue)
    dictionary = {}
    print(f"My   Queue = {myQ}")
    print(f"Your Queue = {yourQ}")
    print(f"My   Activity:Location = {translateNumberToWord(myQ)}")
    print(f"Your Activity:Location = {translateNumberToWord(yourQ)}")
    score = checkQueue(l) 
    if score >=7 :
        print(f"Yes! You're my love! : Score is {score}.")
    elif score < 7 and score > 0:
        print(f"Umm.. It's complicated relationship! : Score is {score}.")
    else :
        print(f"No! We're just friends. : Score is {score}.")
