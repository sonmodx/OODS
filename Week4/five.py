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

def interuptNormal(n,mlist) :
    t,temp = boomThree(mlist)
    item = Queue(temp)
    fail =0
    ls = n
    i = 0
    count =1
    while i < len(ls) :
        if i < len(ls)-1 and str(ls[i]) == str(ls[i+1]) :
            count+=1
        elif i < len(ls)-1 and str(ls[i]) != str(ls[i+1]) :
            count = 1
        if count ==3 :
            count =1
            if not item.isEmpty() :
                if str(ls[i]) == item.peek() :
                    fail+=1
                ls.insert(i+1,item.dequeue())
                
                i+=1
               
        i+=1
    return ls,fail,temp
            
def boomThree(lRev, lss=[]) :
    if lss ==[]:
        ls =[]
    else :
        ls = lss
    
    i =0
    count=1
    while i < len(lRev)-1:
        if str(lRev[i])==str(lRev[i+1]):
            count += 1
        elif str(lRev[i])!=str(lRev[i+1]):
            count =1
        if count ==3:
            count=1
            ls.append(lRev[i])
            lRev.pop(i+1)
            lRev.pop(i)
            lRev.pop(i-1)
            boomThree(lRev,ls)
            
        i+=1
    return lRev,ls


if __name__ =="__main__" :
    n, m = input("Enter Input (Normal, Mirror) : ").split()
    mlist = list(m)
    nlist = list(n)
    mlist.reverse()

    ls,fail,ml = interuptNormal(nlist,mlist) 
    boomLs,lenBoomLs = boomThree(ls)
    print("NORMAL :")
    #len after boom
    print(len(boomLs))
    #show letters after boom
    strNormal = ''.join(reversed(boomLs))
    if strNormal=='':
        print("Empty")
    else :
        print(strNormal)
    #boom
    if fail>0 :
        print(f"{len(lenBoomLs)-fail} Explosive(s) ! ! ! (NORMAL)")
        print(f"Failed Interrupted {fail} Bomb(s)")
    else :
        print(f"{len(lenBoomLs)-fail} Explosive(s) ! ! ! (NORMAL)")
    print("------------MIRROR------------")
    print(": RORRIM")
    #length after boom
    print(len((mlist)))
    strMirror = ''.join(reversed((mlist)))
    #letters after boom
    if strMirror=='':
        print("ytpmE")
    else :
        print(strMirror)
    #boom
    print(f"(RORRIM) ! ! ! (s)evisolpxE {len(ml)}")