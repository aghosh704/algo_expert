def binarySearch(array, target):
    # Write your code here.
    if len(array) <= 0:
        return -1
    mid_point = len(array) // 2
    if array[mid_point] == target:
        print(array, mid_point, target)
        return mid_point
    elif array[mid_point] > target:
        return binarySearch(array[:mid_point], target)
    else:
        tmp = binarySearch(array[mid_point + 1:], target)
        if tmp == -1:
            return -1
        else:
            return tmp + mid_point + 1

array = [1, 5, 23, 111]
print(binarySearch(array, 35))
