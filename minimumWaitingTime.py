def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    sum_arr = 0
    for idx, tmp in enumerate(queries):
        sum_arr += sum(queries[0:idx])
    return sum_arr


print(minimumWaitingTime([3, 2, 1, 2, 6]))