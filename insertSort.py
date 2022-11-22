def insertSort(ls,index) :
    if index >= len(ls) -1 :
        return
    if ls[index] > ls[index+1] :
        ls[index],ls[index+1] = ls[index+1],ls[index]
        goBack(ls,index,index)     
    
    return insertSort(ls, index + 1)

def goBack(ls,index,temp) :
    if index <= 0 :
        return insertSort(ls,temp)
    if ls[index] < ls[index-1] :
        ls[index],ls[index-1] = ls[index-1],ls[index]
    return goBack(ls,index-1,temp)
    
if __name__ == '__main__' :
    inp = [int(a) for a in input("Enter input : ").split()]
    insertSort(inp,0)
    print(inp)