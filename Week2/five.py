def bon(w):
	### Enter Your Code Here ###
    MULTI = 4
    for letter in w:
        if w.index(letter)!=w.rindex(letter):
            break
    asci = ord(letter)
    return (asci-96)*MULTI
    
        
        
secretCode = input("Enter secret code : ")
print(bon(secretCode))