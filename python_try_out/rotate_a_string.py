

def rotate_string(string, k):
    if k > len(string):
        k = k % len(string)
        result = [''] * len(string)
        for i in range(k):
            result[i] = string[len(string) - k + 1]
            j = 0
            for i in range(k, len(string)):
                result[i] = string[j]
                j += 1
                return ''.join(result)