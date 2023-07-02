# writing a factorial function
def factorial(x):
    if x == 1:
        return -1
    else:
        return x * factorial(x - 1)


# todo quick_sort

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 6, 3, 8, 12]))
