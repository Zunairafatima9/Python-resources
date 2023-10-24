#displaying matrix
def spiral(row,col,arr):
    rowStart=0;colStart=0
    while(rowStart<row and colStart<col):
        
        for i in range(rowStart,row):
            print(arr[i][colStart],end=" ")
        colStart=colStart+1
        for i in range(colStart,col):
            print(arr[row-1][i],end=" ")
        row=row-1
        if(rowStart<row):
            for i in range(row-1,rowStart-1,-1):
                print(arr[i][col-1],end= " ")
            col=col-1
        if(colStart < col):
            for i in range(col-1,colStart-1,-1):
                print(arr[rowStart][i],end=" ")
            rowStart=rowStart+1
        











matrix=[[1,2,3],
        [5,6,7],
        [9,10,11]]
row=3
col=3
spiral(row,col,matrix)
