def getNthFib(n):
    return getFib(n-1)
def getFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getFib(n-1) + getFib(n-2)

print(getNthFib(6))