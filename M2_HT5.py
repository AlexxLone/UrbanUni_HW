def get_matrix(n, m, value):
    matrix = list()
    for i in range(0, n):
        matrix.append([])
        for j in range(0, m):
            matrix[i].append(value)
    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
