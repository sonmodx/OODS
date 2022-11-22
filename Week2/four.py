l = []
for number in input("Enter Your List : ").split():
    l.append(int(number))
if len(l) <3:
    print("Array Input Length Must More Than 2")
else :
    ans = []
    for i in range(0,len(l)-2) :
        for j in range(i+1,len(l)-1) :
            for k in range(j+1,len(l)) :
                if l[i] + l[j] + l[k]== 5 :
                    temp = []
                    temp.append(l[i])
                    temp.append(l[j])
                    temp.append(l[k])
                    temp.sort()
                    if ans.__contains__(temp) :
                        continue
                    ans.append(temp)

    print(ans)


