def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    heights = list(zip(redShirtHeights, blueShirtHeights))
    sum_red = 0
    sum_blue = 0
    for height in zip(redShirtHeights, blueShirtHeights):
        if height[0] > height[1]:
            sum_red += 1
        if height[0] < height[1]:
            sum_blue += 1
    if sum_red == len(heights):
        return True
    elif sum_blue == len(heights):
        return True
    else:
        return False



redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

print(classPhotos(redShirtHeights, blueShirtHeights))