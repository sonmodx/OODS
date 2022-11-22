def rfunc(ls, x, y, total) :
    print("xy",x,y)
    if x < len(ls) and y < len(ls):
        ##case .. 
        return rfunc(ls, x*2+1, y*2+2, total+ls[x]+ls[y])
    if x < len(ls):
        ##case .. 
        return rfunc(ls, x*2+1, y, total+ls[x])
    if y < len(ls):
        ##case .. 
        return rfunc(ls, x, y*2+2, total+ls[y])
    return total
    

if __name__=='__main__' :
    ls = [5,4,2,3,1] 
    pos = 0
    res = rfunc(ls ,pos*2+1 ,pos*2+2 , ls[pos])
    print(res)
    
    