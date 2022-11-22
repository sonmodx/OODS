def findMinweight(ls, numBox, mini):
    weight = 0
    countBox = 0
    for item in ls :
        if weight + item <= mini :
            weight += item
        else :
            countBox += 1
            weight = item
    if countBox + 1 == numBox :
        return mini
    return findMinweight(ls, numBox, mini + 1)


if __name__ =='__main__' :
    ls, box = input("Enter Input : ").split('/')
    ls = [int(a) for a in ls.split()]
    print(f'Minimum weigth for {box} box(es) = {findMinweight(ls, int(box), max(ls))}')