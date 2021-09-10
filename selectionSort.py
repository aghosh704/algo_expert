def selectionSort(array):
    min = float('inf')

    curr_idx = 0
    while curr_idx < len(array):
        idx = curr_idx
        min = float('inf')
        min_idx = -1
        while idx < len(array):
            if array[idx] < min:
                min = array[idx]
                min_idx = idx
            idx += 1
        swap(array, curr_idx, min_idx)
        curr_idx += 1
    return array
def swap(array, i, j):

    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

print(selectionSort([2, 5, 8, 9, 5, 6, 3]))