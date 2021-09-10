def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    first_ptr = 0
    second_ptr = 0
    min_delta = float('inf')
    res = [-1, -1]

    while True:
        v1 = arrayOne[first_ptr]
        v2 = arrayTwo[second_ptr]

        if abs(v1) == abs(v2):
            res[0] = v1
            res[1] = v2
            break
        else:
            curr_delta = abs(v1-v2)
            if curr_delta < min_delta:
                res[0] = v1
                res[1] = v2
                min_delta = curr_delta
            else:
                pass

            if v1 < v2:
                first_ptr += 1
            elif v1 > v2:
                second_ptr += 1
        if first_ptr > len(arrayOne)-1:
            break;

        if second_ptr > len(arrayTwo) - 1:
            break;
    return res

print(smallestDifference([-1, 5, 10, 20, 28, 2], [26, 34, 135, 15, 17]))