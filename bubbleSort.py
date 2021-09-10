def bubbleSort(array):
    # Write your code here.
    swap = 0
    while True:

        for idx, elem in enumerate(array):
            if idx + 1 < len(array):

                if array[idx] > array[idx + 1]:
                    swap += 1
                    tmp = array[idx]
                    array[idx] = array[idx + 1]
                    array[idx + 1] = tmp
        if swap == 0:
            break
        else:
            swap = 0
    return array


myarray = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(myarray))