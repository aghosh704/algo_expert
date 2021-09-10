def insertionSort(array):
    boundary = 0
    for idx, num in enumerate(array):
        if idx > 0:
            j = 0
            while j < idx:
                if array[j] > array[idx]:
                    swap(array, idx, j)
                j += 1
    #swap(array, 3,4)
    print(array)
def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

insertionSort([99, 98, 1, 76])