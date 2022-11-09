def zero_matrix(m):
    row_length = len(m)
    col_length = len(m[0])
    zeros_pos = []

    for i in range(row_length):
        for j in range(col_length):
            if m[i][j] == 0:
                zeros_pos.append((i, j))

    for pos in zeros_pos:
        for i in range(row_length):
            m[i][pos[1]] = 0
        for i in range(col_length):
            m[pos[0]][i] = 0

    return m 

print(zero_matrix([[5, 5, 5, 5], [5, 0, 5, 5], [8, 8, 8, 8], [3, 3, 3, 0]]))

def zero_matrix_solution(m):
    row_length = len(m)
    col_length = len(m[0])
    row_zeros = [False] * row_length
    col_zeros = [False] * col_length

    for i in range(row_length):
        for j in range(col_length):
            if m[i][j] == 0:
                row_zeros[i] = True
                col_zeros[j] = True

    for i in range(row_zeros):
        if row_zeros[i]:
            for j in range(col_length):
                m[i][j] = 0

    for j in range(col_zeros):
        if col_zeros[j] == 0:
            for i in range(row_length):
                m[i][j] = 0

    return m

print(zero_matrix([[5, 5, 5, 5], [5, 0, 5, 5], [8, 8, 8, 8], [3, 3, 3, 0]]))

