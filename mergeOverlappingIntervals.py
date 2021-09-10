def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x:x[0])
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
    return mergedIntervals

intervals = [
    [1,5],
    [3, 6],
    [7,8],
    [9, 13],
    [11, 12],
    [33, 55]
]

print(mergeOverlappingIntervals(intervals))