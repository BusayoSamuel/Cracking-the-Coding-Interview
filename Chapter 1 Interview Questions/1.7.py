"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
the image by 90 degree. Can you do this in place?
"""

"""
def rotate_matrix(s):
    n = len(s)

    output_matrix[[[None] * n]*n]

    for i in range(len(s)):
        for j in range(len(i)):
            output_matrix[i]
"""

def rotate_matrix(m):
    n = len(m)

    if n == 0 or n != len(m[0]):
        return False

    for i in range(n):
        for j in range(i, n):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp

    for i in range(n):
        for j in range(n//2):
            temp = m[i][j]
            m[i][j] = m[i][n-1-j]
            m[i][n-1-j] = temp

    return m

print(rotate_matrix([[3, 2, 5, 7], [5, 6, 3, 4], [8, 9, 2, 1], [0, 6, 7, 9]]))


def rotate_matrix_solution(m):
    if len(m) == 0 or len(m) != len(m(0)):
        return False

    layers = len(m)

    for layer in range(layers):
        first = layer
        last = layers - 1 - layer

        for i in range(first, last):
            offset = 
            #save the top
            temp = m[first][i]

            #left to top
            m[first][i] = m[last][i]

            #bottom to left
            m[]