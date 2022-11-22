def sortHighToLow(start,end,ls,r) :
    if r == end :
        return
    if start ==end :
        return sortHighToLow(0,end,ls,r+1)
    if ls[start] < ls[start+1]:
        ls[start],ls[start+1] = ls[start+1],ls[start]
    if start < end :
        return sortHighToLow(start+1,end,ls,r)



if __name__ == "__main__":
    ls = [int(a) for a in input("Enter your List : ").split(',')]
    sortHighToLow(0,len(ls)-1,ls,0)
    print("List after Sorted :",ls)