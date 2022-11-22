print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
bound = 1
for i in range(n-1) :
    bound +=4
sign = "#"
signLeftandRight = "#"
start =0
goBack =0
count=0
end = bound
for i in range(bound):
    for x in range(0,count):
        if x%2==0:
            signLeftandRight="#"
        else :
            signLeftandRight="."
        print(signLeftandRight,end="")
    for j in range(start,end):
        print(sign,end="")
    for k in reversed(range(0,count)):
        if k%2==0:
            signLeftandRight="#"
        else :
            signLeftandRight="."
        print(signLeftandRight,end="",sep="")
    if i%2==0:
        sign="."
    else :
        sign="#"
    print("")
    if goBack==0 and start < end:
        start+=1
        end-=1
        count+=1
    if start >= end and goBack==0:
        start =1
        end =4
        goBack=1
        count-=2
    elif goBack==1:
        start-=1
        end+=1
        count-=1