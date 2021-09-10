def firstDuplicateValue(array):
    # Write your code here.
    charmap = {}
    for tmp in array:
        if tmp in charmap:
            return tmp
        else:
            charmap[tmp] = tmp

a = [2, 1, 5, 2, 3, 3, 4]

print(firstDuplicateValue(a))
