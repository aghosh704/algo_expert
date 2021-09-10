def firstNonRepeatingCharacter(string):
    from  collections import OrderedDict
    cnts_map = OrderedDict()
    array = [s for s in string]
    for s in array:
        cnts_map[s] = cnts_map.setdefault(s, 0) + 1
    for k,v in cnts_map.items():
        print(k, v)
        if v <= 1:
            return array.index(k)
    return -1
    

print(firstNonRepeatingCharacter("coolcode"))