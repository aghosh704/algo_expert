
def isMonotonic(array):

    return non_decreasing(array) or non_decreasing(array)

def non_increasing(L):
    return all(x>=y for x, y in zip(L, L[1:]))

def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))