def printNumber(end) :
    if end < 0:
        return
    binary = str(bin(end)[2:])
    t = "0"*(len(binary)) + binary
    print("HI")
    printNumber(end-1)
    print(t)
    return 

if __name__ == "__main__":
    number = int(input("Enter Number : "))
    if number < 0 :
        print("Only Positive & Zero Number ! ! !")
    else :
        number = (2**number)-1
        printNumber(number)
