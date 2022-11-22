def fact(n) :
    if n<=1:
        return 1
    return fact(n-1)*n

if __name__ == "__main__" :
    n = int(input("Enter Number : "))
    ans = fact(n)
    print(f"{n}! = {ans}")