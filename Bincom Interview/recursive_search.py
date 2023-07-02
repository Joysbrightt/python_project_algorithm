
def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return False

    if numbers[index] == target:
        return True

    return recursive_search(numbers, target, index + 1)


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    try:
        target_number = int(input("Enter a number to search: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

result = recursive_search(number_list, target_number)
if result:
    print("Number found in the list!")
else:
    print("Number not found in the list.")
