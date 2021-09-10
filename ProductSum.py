# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    return productSumHelper(array, 0, 1)


def productSumHelper(array, sum_so_far, level):
    for elem in array:
        if isinstance(elem, list):
            tmp = productSumHelper(elem, 0, level + 1)
            sum_so_far = sum_so_far + tmp
        else:
            sum_so_far = sum_so_far + elem
    return sum_so_far * level


arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
#arr = [[6, [-13, 8], 4]]


print(productSum(arr))
