def checkio(matrix):
    #replace this for solution

    for rowdata in matrix:
        for i in range(len(rowdata) -3):
            # print(str(rowdata[i]) + ":" + str(rowdata[i+1]) + ":" + str(rowdata[i+2]) + ":" + str(rowdata[i+3]))
            if rowdata[i] == rowdata[i+1] == rowdata[i+2] == rowdata[i+3]:
                return True

    for i in range(len(matrix)-3):
        for j in range(len(matrix[i])):
            if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]:
                return True

    x = len(matrix)
    y = len(matrix[0])

    for i in range(x-3):
        for j in range(y-3):
            if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]:
                return True

    for k in range(x-3):
        for l in range(y-1, y-4, -1):
            print(str(k) + ":" + str(l))
            if matrix[k][l] == matrix[k+1][l-1] == matrix[k+2][l-2] == matrix[k+3][l-3]:
                return True

    return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print(checkio([
    #     [1, 2, 1, 1],
    #     [1, 1, 4, 1],
    #     [1, 3, 1, 6],
    #     [1, 7, 2, 5]
    # ]))# == True, "Vertical"
    # print(checkio([
    #     [7, 1, 4, 1],
    #     [1, 2, 5, 2],
    #     [3, 4, 1, 3],
    #     [1, 1, 8, 1]
    # ]))# == False, "Nothing here"
    # print(checkio([
    #     [2, 1, 1, 6, 1],
    #     [1, 3, 2, 1, 1],
    #     [4, 1, 1, 3, 1],
    #     [5, 5, 5, 5, 5],
    #     [1, 1, 3, 1, 1]
    # ]))# == True, "Long Horizontal"
    # print(checkio([
    #     [7, 1, 1, 8, 1, 1],
    #     [1, 1, 7, 3, 1, 5],
    #     [2, 3, 1, 2, 5, 1],
    #     [1, 1, 1, 5, 1, 4],
    #     [4, 6, 5, 1, 3, 1],
    #     [1, 1, 9, 1, 2, 1]
    # ]))# == True, "Diagonal"

    print(checkio([[7,9,1,7,6,7,5,9,6],
                   [5,5,9,3,1,6,7,4,7],
                   [1,7,5,2,3,1,6,4,7],
                   [2,2,2,8,7,2,6,6,9],
                   [5,6,4,2,6,7,3,4,7],
                   [5,5,6,4,9,4,3,1,7],
                   [7,3,2,3,2,4,4,7,3],
                   [3,6,9,7,2,5,6,2,5],
                   [4,1,3,9,4,2,4,8,4]]))

