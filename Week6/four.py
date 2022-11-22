def subset(nums) :
    output =[[]]
    for i in nums:
        output += [lst + [i] for lst in output] 
    return output

def findMinimum(ss,minimum) :
    for val in ss :
        if len(val) >=1:
            sumS,sumB = 1,0
            s = [int(a.split(' ')[0]) for a in val]
            b = [int(a.split(' ')[1]) for a in val]
            for val in s :
                sumS = sumS * val
            for val in b :
                sumB += val
            absDistance = abs(sumS-sumB)
            if absDistance < minimum :
                minimum = absDistance
                
    return  minimum

if __name__ =="__main__":
    ls = input("Enter Input : ").split(',')
    ss = subset(ls)
    m = findMinimum(ss,1000000000)
    print(m)

    
