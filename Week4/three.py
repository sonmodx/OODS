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

def encodemsg(q1,q2) :
    output = Queue()
    while not q1.isEmpty():
        if q1.peek().isalpha():
            shift = int(q2.dequeue())
            letter = ""
            if ord(q1.peek())+shift > ord('z'):
                letter = ord(q1.dequeue()) + shift - 26
                output.enqueue(chr(letter))
            elif ord(q1.peek())+shift > ord('Z') and q1.peek().isupper():
                letter = ord(q1.dequeue()) + shift - 26
                output.enqueue(chr(letter))
            else :
                letter = ord(q1.dequeue()) + shift
                output.enqueue(chr(letter))
            q2.enqueue(shift)
        else :    
            q1.dequeue()
    return output

def decodemsg(q1,q2) :
    output = Queue()
    while not q1.isEmpty():
        if q1.peek().isalpha():
            shift = int(q2.dequeue())
            letter = ""
            if ord(q1.peek())-shift < ord('a') and q1.peek().islower():
                letter = ord(q1.dequeue()) - shift + 26
                output.enqueue(chr(letter))
            elif ord(q1.peek())-shift < ord('A') and q1.peek().isupper():
                letter = ord(q1.dequeue()) - shift + 26
                output.enqueue(chr(letter))
            else :
                letter = ord(q1.dequeue()) - shift
                output.enqueue(chr(letter))
            q2.enqueue(shift)
        else :    
            q1.dequeue()
    return output

if __name__ == "__main__":
    string,number = input("Enter String and Code : ").split(",")
    q1 = Queue(string)
    q2 = Queue(number)
    q1 = encodemsg(q1,q2)
    print("Encode message is : ",q1)
    q2 = Queue(number)
    print("Decode message is : ",decodemsg(q1, q2))