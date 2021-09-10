def threeNumberSum(array, targetSum):
    array = sorted(array)
    print ("sorted array {}".format(array))
    result =[]
    for current_ptr, val in enumerate(array):
        left_ptr = current_ptr + 1
        right_ptr = len(array) - 1
        while True:
            if left_ptr >= right_ptr:
                break
            if right_ptr < 0:
                break
            if left_ptr > len(array)-1:
                break

            this_sum = array[current_ptr] + array[left_ptr] + array[right_ptr]
            print(
                "Comparing sum of {} from indexes {}, {}, {} with target of {}".format(this_sum, current_ptr, left_ptr, right_ptr,  targetSum))

            if this_sum > targetSum:
                right_ptr -= 1
            if this_sum < targetSum:
                left_ptr += 1

            if this_sum == targetSum:
                result.append([array[current_ptr], array[left_ptr], array[right_ptr]])
                right_ptr -= 1
                left_ptr += 1

    return result

tup = threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(tup)