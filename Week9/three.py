def checkDescending(ls) :
    check = None
    for i in range(0,len(ls)-1) :
        if (check is False and ls[i] < ls[i+1]) or (check is True and ls[i] > ls[i+1]):
            return None
        if ls[i] > ls[i+1] :
            check = False
        if ls[i] < ls[i+1] :
            check = True
    return check

def checkSame(ls) :
    for i in range(0,10) :
        if ls.count(i) == len(ls) :
            return True ,True
        if ls.count(i) > 1 :
            return True ,False
    return False,False

if __name__=='__main__' :
    number = input("Enter Input : ")
    ls = []
    for digit in number :
        ls.append(int(digit))
    isDescending = checkDescending(ls)
    isSame,isAllSame = checkSame(ls)
    if isDescending is not None :
        if isDescending and not isSame :
            print("Metadrome")
        elif isDescending and isSame :
            print("Plaindrome")
        elif not isDescending and not isSame:
            print("Katadrome")
        elif not isDescending and isSame :
            print("Nialpdrome")
    elif isAllSame :
        print("Repdrome")
    else :
        print("Nondrome") 
    