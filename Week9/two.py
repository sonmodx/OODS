def findMax(ls,left,right,element) :
    if left <=right :
        if ls[left] > element :
            return findMax(ls,left+1,right,ls[left])
        else :
            return findMax(ls,left+1,right,element)
    return element

def selectSort(ls, last) :
    if last < 1 :
        return
    maxElement = findMax(ls,0,last,ls[0])
    
    indexOfMax = ls.index(maxElement)
    if ls[last] < ls[indexOfMax] :
        ls[last],ls[indexOfMax] = ls[indexOfMax],ls[last]
        maxVal = ls[indexOfMax]
        minVal = ls[last]
        if ls[last] > ls[indexOfMax] :
            maxVal =ls[last]
            minVal =ls[indexOfMax]
        print("swap {} <-> {} : {}".format(minVal,maxVal,ls))
    selectSort(ls, last - 1)
if __name__ == '__main__' :
    inp = [int(item) for item in input("Enter Input : ").split()]
    selectSort(inp, len(inp)-1)
    print(inp)