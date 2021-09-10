def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):

    if (fastest):
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
    max_speed = 0
    team = zip(redShirtSpeeds, blueShirtSpeeds)
    for tmp in team:
        max_speed += max(tmp[0], tmp[1])
    return max_speed


redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, True))
