def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix1 = []
        for j in range(m):
            matrix1.append(value)
        matrix.append(matrix1)

    return matrix

res1 = get_matrix(2,2,10)
res2 = get_matrix(3,5,42)
res3 = get_matrix(4,2,13)

print(res1)
print(res2)
print(res3)

