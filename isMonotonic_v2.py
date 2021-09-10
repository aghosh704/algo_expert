
def isMonotonic(array):
    pos_cntr = 0
    neg_cntr = 0
    for idx, val in enumerate(array):
        if (idx <= len(array)-2):
            if array[idx + 1] >= array[idx]:
                pass
            else:
                pos_cntr += 1
            if array[idx + 1] <= array[idx]:
                pass
            else:
                neg_cntr += 1

    return pos_cntr == 0 or neg_cntr == 0

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))