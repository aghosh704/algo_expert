def generateDocument(characters, document):
    charmap = {}
    for c in characters:
        charmap[c] = charmap.setdefault(c, 0) + 1
    if len(characters) == 0:
        return False
    if (len(document) == 0):
        return True

    for d in document:
        if d in charmap:
            if (charmap[d] <= 0):
                return False;
            else:
                charmap[d] -= 1
        else:
            return False
    return True

print(generateDocument('abccdefa', 'abxc'))
