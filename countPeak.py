
def longestPeak(array):

    if len(array) == 0:
        return 0
    peak = []
    for idx, tmp in enumerate(array):
        if (idx >= 1) and (idx <= len(array)-2):
            if (array[idx - 1] < array[idx]) and (array[idx] > array[idx + 1]):
                peak.append(idx)

    #print(peak)
    peak_length = []
    for tmp in peak:

        left = tmp
        right = tmp
        cntr = 1
        while left-1 >= 0:

            if array[left-1] < array[left]:
                cntr += 1
                left -=1
                #print("left", tmp, cntr)
            else:
                break
            while right+1 <= len(array)-1:

                if array[right+1] < array[right]:
                    cntr += 1
                    right +=1
                    #print("right", tmp, cntr)
                else:
                    break

        peak_length.append(cntr)
    return 0 if len(peak_length) == 0 else max(peak_length)
#a = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
a = [1,3,2]

print(longestPeak(a))