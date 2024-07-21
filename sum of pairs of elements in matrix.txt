# Find pairs of numbers from the given matrix where the sum of them equals 11 and the elements of the pair are in different # rows of the matrix
# Expected Output: (1, 10), (3, 8), (2, 9), (4, 7), (11, 0) 
# sum of elements = 11

mat = [[1, 3, 2, 4],
                     [5, 8, 7, 6],
                     [9, 10, 13, 11],
                     [12, 0, 14, 15]]
                     
# print(type(mat))    # <class 'list'>

n_row = len(mat)    # to find no of rows in Python matrix/2 d list
n_col = len(mat[0]) # to find no. of columns in Python matrix/2 d list

# print(n_row)
# print(n_col)

for i in range(0, n_row):
    for j in range(0, n_col):
        for k in range(0, n_row):
            for l in range(0, n_col):
                if mat[i][j] + mat[k][l] == 11:
                    print(mat[i][j], " & ", mat[k][l])
                

# this code works well but produces repetitive results
________________________________________________________________________________________________________

# this code works well

mat = [[1, 3, 2, 4],
                     [5, 8, 7, 6],
                     [9, 10, 13, 11],
                     [12, 0, 14, 15]]
                     
n_row = len(mat)    # to find no of rows in Python matrix/2 d list
n_col = len(mat[0]) # to find no. of columns in Python matrix/2 d list

# print(n_row)
# print(n_col)

for i in range(0, n_row):
    for j in range(0, n_col):
        for k in range(i+1, n_row):
            for l in range(0, n_col):
                if k == n_row :
                    break # this ensures that the index does not go out of bounds

                else:
                    if mat[i][j] + mat[k][l] == 11:
                        print(mat[i][j], " & ", mat[k][l])


