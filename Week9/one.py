def mergeSort(ls) :
    if len(ls) <= 1:
        return
    mid = len(ls) // 2
    leftList = ls[0:mid]
    rightList = ls[mid::]
    mergeSort(leftList)
    mergeSort(rightList)
    merge(ls,leftList,rightList)

def merge(ls,leftList,rightList) :
    i,j,k = 0,0,0
    while i < len(leftList) and j < len(rightList) :
        if leftList[i] >= rightList[j] :
            ls[k] = rightList[j]
            j+=1
            k+=1
        else :
            ls[k] = leftList[i]
            i+=1
            k+=1
    while i < len(leftList) :
        ls[k] = leftList[i]
        k+=1
        i+=1
    while j < len(rightList) :
        ls[k] = rightList[j]
        k+=1
        j+=1


if __name__ =='__main__' :
    inp = [int(item) for item in input("Enter Input : ").split()]
    temp = inp[::]
    mergeSort(inp)
    print("Yes") if temp==inp else print("No")