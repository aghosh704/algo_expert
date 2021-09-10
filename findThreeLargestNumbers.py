def findThreeLargestNumbers(array):
    # Write your code here.
    large = [float('-inf')] * 3
    for num in array:
        if num > large[2]:
            large[0] = large[1]
            large[1] = large[2]
            large[2] = num
        elif (num <= large[2]) and (num > large[1]):
            large[0] = large[1]
            large[1] = num
        elif (num <= large[1]) and (num > large[0]):
            large[0] = num
    return large


array = [7, 7, 7, 7]
print(findThreeLargestNumbers(array))
