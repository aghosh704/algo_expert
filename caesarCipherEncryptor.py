def caesarCipherEncryptor(string, key):
    cntr = 1
    char_idx = {}
    idx_char = {}
    encrypted = []
    for s in "abcdefghijklmnopqrstuvwxyz":
        char_idx[s] = cntr
        idx_char[cntr] = s
        cntr += 1
    for s in string:
        new_val = char_idx[s] + key
        if new_val > 26:
            new_val = new_val % 26
        encrypted.append(idx_char[new_val])
    return "".join(encrypted)

print(caesarCipherEncryptor('abz', 53))