

def longest_palindrome(s):
    max_palindrome_length = 0
    longest_palindrome = None
    length = len(s)

    for i in range(length):
        for j in range(i + 1, length):
            current = s[i:j + 1]
            if is_palindrome(current):
                palindrome_length = len(current)
                if palindrome_length > max_palindrome_length:
                    longest_palindrome = current
                    max_palindrome_length = palindrome_length

    return longest_palindrome


def is_palindrome(s):
    return s == s[:: -1]