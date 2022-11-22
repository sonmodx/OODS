print("*** Fun with countdown ***")
l=[]
for number in input("Enter List : ").split() :
    l.append(int(number))
ans,cur,temp=[],[],[]
count =0
isLessThan = 0
i=0
while i<len(l) :
    if i<len(l)-1 and (l[i]-1==l[i+1]):
        temp.append(l[i])
        isLessThan=1
    elif l[i]==1 and isLessThan==0:
        temp.append(l[i])
        cur.append(temp)
        temp=[]
        count+=1
    elif isLessThan==1 :
        temp.append(l[i])
        count+=1
        isLessThan=0
        if temp!=[]:
            cur.append(temp)
            temp=[]
    i+=1

ans.append(count)
ans.append(cur)

print(ans)


        