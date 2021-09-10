def spiralTraverse(array):
    spiral = []
    rows = len(array)  # 4
    cols = len(array[0])  # 5
    row_start = 0
    col_start = 0
    row_end = len(array) - 1
    col_end = len(array[0]) - 1
    while (row_start <= row_end) and (col_start <= col_end):

        for col in range(col_start, col_end + 1):
            spiral.append(array[row_start][col])

        for row in range(row_start + 1, row_end + 1):
            spiral.append(array[row][col_end])

        if row_start == row_end:
            break
        for col in reversed(range(col_start, col_end)):
            spiral.append(array[row_end][col])
        if col_start == col_end:
            break
        for row in reversed(range(row_start + 1, row_end)):
            spiral.append(array[row][col_start])

        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1
    return spiral


array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]
print(spiralTraverse(array))
