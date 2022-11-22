def staircase(n,right):
    if n ==  0 and right >0:
        return 
    if right ==0 :
        return
    rect = '#'
    under = '_'
    print(under*abs(n-1)+rect*(abs(right)))
    return staircase(n-1,right+1)

if __name__ == "__main__" :
    n = int(input("Enter Input : "))
    if n==0 :
        print("Not Draw!")
    elif n > 0:
        staircase(n, 1)
    else :
        staircase(1, n)