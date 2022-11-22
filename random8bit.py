import random

def random8bit() :
    randomNumber = random.randint(0,255)
    binary = str(bin(randomNumber))[2:]
    #fill in zeroes
    maxLength = 8
    zeroes = "0" * (maxLength - len(binary))
    binary = zeroes + binary
    return binary, randomNumber

if __name__ =='__main__' :
    bi1 ,dec1= random8bit()
    bi2 ,dec2= random8bit()
    totalDec = dec1+dec2
    print("Answer :",hex(totalDec)[2:])
    for i in range(0,15) :
        print("|")
    print(bi1 ,"+", bi2)
    
