def isPalindrome(string):
    idx_1 = 0
    idx_2 = len(string)-1
    if (len(string) <= 1):
        return True
    is_palindrome = True
    while (is_palindrome) and (idx_2>=0) and (idx_1 < len(string)):
        if string[idx_1] == string[idx_2]:
            idx_1 += 1
            idx_2 -= 1
        else:
            is_palindrome = False
    return is_palindrome

print(isPalindrome("a1231a"))