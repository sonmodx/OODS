class Stack:
    def __init__(self,ls=None):
        if ls is None:
            self.ls  = []
        else:
            self.ls = ls
    
    def push(self,value):
        self.ls.append(value)

    def pop(self):
        return self.ls.pop()

    def peek(self):
        return self.ls[-1]

    def isEmpty(self):
        return self.ls == []

    def size(self):
        return len(self.ls)

    def conditions(self,o,value,m,s):
        if o=="arrive":
            if value in s :
                return f"car {value} already in soi"

            if self.size()<m and n not in s:
                self.push(value)
                return f"car {value} arrive! : Add Car {value}"
            return f"car {value} cannot arrive : Soi Full"

        if o=="depart":
            if value not in s and self.size()>0:
                return f"car {value} cannot depart : Dont Have Car {value}"

            if self.size()!=0:
                for i in range(len(s)):
                    if int(s[i]) ==int(value):
                        self.ls.pop(i)
                return f"car {value} depart ! : Car {value} was remove"
            return f"car {value} cannot depart : Soi Empty"

    def __str__(self):
        return str(self.ls)


if __name__ == "__main__":
    print("******** Parking Lot ********")
    m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
    m,n = int(m),int(n)
    if ',' in s :
        s = list(int(a) for a in s.split(','))
    elif int(s)==0:
        s=[]
    st= Stack()
    for car in s:
        st.push(int(car))
    
    print(st.conditions(o,n,m,s))    
    print(st)