
def rotate(num, k):
    if k > len(num):
        k = k % len(num)
        result = [0] * len(num)
        for i in range(k):
            result[i] = num[len(num) - k + i ]
        j = 0
        for i in range(k, len(num)):
            result[i] = num[j]
            j += 1
            num[:] = result
