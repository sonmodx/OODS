print("*** Reading E-Book ***")
l = []
for text in input("Text , Highlight : ").split(","):
    l.append(text)
target = l[1]
for ch in l[0] :
    if ch== target:
        print("[",ch,"]",end="",sep="")
    else :
        print(ch,end="")
