def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x:x[0])
    merged = []
    last_start, last_end = sortedIntervals[0]
    for i, tmp in enumerate(sortedIntervals):
        this_start, this_end = tmp
        if (this_start >= last_start) and (this_start <= last_end):
            last_end = max(last_end, this_end)
            if i == len(sortedIntervals) - 1:
                merged.append([last_start, last_end])
        else:
            merged.append([last_start, last_end])
            if i == len(sortedIntervals) - 1:
                merged.append([this_start, this_end])
            last_start = this_start
            last_end = this_end

    return merged
intervals = [
    [1,2],
    [3, 8],
    [9, 10]
]

print(mergeOverlappingIntervals(intervals))