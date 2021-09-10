def moveElementToEnd(array, toMove):
    left_ptr = 0
    right_ptr = len(array) - 1

    while True:
        while (array[right_ptr] == toMove) & (right_ptr >= 0) & (left_ptr < right_ptr):
            right_ptr -= 1

        if array[left_ptr] == toMove:
            array[left_ptr] = array[right_ptr]
            array[right_ptr] = toMove
            left_ptr += 1
            right_ptr -= 1
        else:
            left_ptr += 1
        if left_ptr >= right_ptr:
            break
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
