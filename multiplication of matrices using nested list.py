A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]
result = []

for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        s = 0
        for k in range(len(B)):
            s += A[i][k] * B[k][j]
        row.append(s)
    result.append(row)

for r in result:
    print(r)