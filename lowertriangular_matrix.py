arr = [[1, 2, 3],
       [4, 5, 6],
       [1, 8, 5]]
def lowertriangular_matrix(arr):
    result=[]
    for i in range(len(arr)):
        row=[]
        for j in range(len(arr[i])):
            if (i>=j):
                row.append(str(arr[i][j]))
            else:
                row.append('0')
        result.append(' '.join(row))

    return result

print(lowertriangular_matrix(arr))