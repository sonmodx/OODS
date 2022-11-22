if __name__ =="__main__" :
    data, x = input("Enter Input : ").split('/')
    dataList = list(map(int,data.split()))
    xList = list(map(int,x.split()))
    for item in xList :
        check = False
        for value in sorted(dataList) :
            if item < value :
                print(value)
                check = True
                break
        if not check :
            print("No First Greater Value")
