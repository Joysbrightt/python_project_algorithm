# binary_search todo log2 n
# todo Big O notation lets you compare the number of operations. It
# todo tells you how fast the algorithm grows.
import item as item


#
# low = 0
# high = len(lst) - 1
# mid = (low + high) / 2
# guess = lst[mid]
#
# if guess < item:
#     low = mid + 1

def binary_search(arr, element):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == element:
            return mid

        if guess > element:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 7))


def binary_search(arr, oja):
    low = 0
    high = len(arr - 1)

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == oja:
            return mid
        if guess < oja:
            high = mid - 1

        if guess > oja:
            mid = high - 1

        else:
            low = mid + 1
            return None
