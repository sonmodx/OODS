def range(a=0,b=0,c=1) :
    start = a
    end = b
    incre = c
    print("(",end="")
    
    while start<end :
        isFloat = 0
        num = ("%f" %start).rstrip('0').rstrip('.')
        convert_str = str(num)
        if convert_str.find('.')!=-1 :
            isFloat =1
        if isFloat==1:
            print(num,end="")
        else :
            print("%.1f" %float(num),end="")
        
        
        start+=incre
        if start<end :
            print(", ",end="")
    print(")",end="")

print("*** New Range ***")
l = []
for number in input("Enter Input : ").split() :
    l.append(float(number))
if len(l)==1:
    range(0,l[0])
elif len(l)==2:
    range(l[0],l[1])
else :
    range(l[0],l[1] ,l[2])



