def ZeroMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    store = []
    print("Matrix Before:")
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                store += [i, j]
            print(matrix[i][j], end=" ")
        print()
    print(store)

    for k in range(len(store)):
        if k % 2 == 0:
            for i in range(len(matrix)):
                print(store[k])
                matrix[store[k]][i] = 0
        else:
            for i in range(len(matrix[0])):
                print(store[k])
                matrix[i][store[k]] = 0

    print("\n\n",matrix)
    print("Matrix After:")
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()


matrix = [[0, 2, 3], [4, 1, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 1, 6], [7, 0, 9]]
ZeroMatrix(matrix)
ZeroMatrix(matrix2)
