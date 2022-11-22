def bi_search(l, r, arr, x):
    if l <= r :
        mid = l + (r - l)// 2
        if arr[mid] == x :
            return True
        if arr[mid] < x :
            return bi_search(mid+1,r,arr,x)
        else :
            return bi_search(l,mid-1,arr,x)
    return False 


if __name__ =="__main__" :
    inp = input('Enter Input : ').split('/')
    arr, k = list(map(int, inp[0].split())), int(inp[1])
    print(bi_search(0, len(arr) - 1, sorted(arr), k))
