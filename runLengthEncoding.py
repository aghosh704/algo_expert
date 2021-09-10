def runLengthEncoding(string):
    cntr = 0
    last_char = string[0]
    encoding = []
    for s in string:
        if (s == last_char) & (cntr <= 8):
            cntr += 1
        else:
            encoding.append(str(cntr) + last_char)
            cntr = 1
        last_char = s
    encoding.append(str(cntr) + last_char)
    return ''.join(encoding)
        
x = runLengthEncoding("aaaaabbbbbbbbbbcckk")
print(x)