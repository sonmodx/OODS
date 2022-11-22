def findAlphabet(word) :
    for letter in word :
        if letter.isalpha() :
            return letter
    return 

def specialSort(ls) :
    for i in range(0,len(ls)) :
        for j in range(0,len(ls)-i-1) :
            firstLetter = findAlphabet(ls[j])
            secondLetter = findAlphabet(ls[j+1])
            if firstLetter >= secondLetter :
                ls[j],ls[j+1] = ls[j+1],ls[j]

if __name__ =='__main__' :
    inp = input("Enter Input : ").split()
    specialSort(inp)
    print(str(inp)[1:-1].replace('\'','').replace(',',''))