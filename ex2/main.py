def main():
    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]
    gameOfLive(matrix)

def nearbyCounter(i, j , colLen, rowLen, matrix):
    count = 0
    y = -1
    while y <= 1:
        x = -1
        while x <= 1:
            if not (x == 0 and y == 0):
                cx = y + i
                cy = x + j
                if 0 <= cx < colLen and 0 <= cy < rowLen:
                    count += matrix[cy][cx]
            x +=1
        y += 1
    return count


def gameOfLive(matrix):
    for _ in range(5):
        colLen = len(matrix)
        rowLen = len(matrix[0])

        nextState = [[0]*rowLen for _ in range(colLen)]
        i = 0
        while i < colLen:
            j = 0
            while j < rowLen:
                nb = nearbyCounter(i, j , colLen, rowLen, matrix)
                if matrix[j][i] == 1:
                    if nb == 2 or nb == 3:
                        nextState[j][i] = 1
                else:
                    if nb == 3:
                        nextState[j][i] = 1
                j += 1
            i += 1
        matrix = nextState
        
    # for row in matrix:
    #    print(row)

if __name__ == "__main__":
    main()