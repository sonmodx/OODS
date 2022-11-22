print("*** multiplication or sum ***")
l = []
for num in input("Enter num1 num2 : ").split():
    l.append(num)
ans = int(l[0])*int(l[1])

if ans > 1000 :
    ans=int(l[0])+int(l[1])
print("The result is %d" %(ans))