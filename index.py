if __name__ =='__main__' :
    A = [
        [1,2],
        [4,5],
        [7,8]
    ]
    B = [
        [1,2,1,1],
        [3,5,2,1]
    ]
    #multiplication matrix
    #A * B
    M = []
    for i in range(0,len(A)) :
        temp = []
        for j in range(0,len(B[0])) :
            total = 0
            
            for k in range(0,len(A[0])) :
                total += A[i][k] * B[k][j]
            temp.append(total)
        M.append(temp)
    print("matrix M")
    for i in range(0,len(M)) :
        for j in range(0,len(M[0])) :
            print(M[i][j],end=' ')
        print()
    


    