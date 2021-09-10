def arrayOfProducts(array):
    product_l = 1
    product_r = 1
    left = [1 for i in array]
    right = [1 for i in array]
    idx = 1
    while idx <= len(array)-1:
        product_l = product_l * array[idx - 1]
        left[idx] = product_l
        idx += 1

    idx = len(array)-2
    while idx >= 0:
        product_r = product_r * array[idx + 1]
        right[idx] = product_r
        idx -= 1
    return [a*b for a,b in zip(left,right)]
a = [1, 8, 6, 2, 4]

print(arrayOfProducts(a))
#print(4 // 2)