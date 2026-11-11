
def sum_array(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_array(numbers[1:])


def find_largest(numbers):
    if len(numbers) == 0:
        raise ValueError("Array must not be empty")
    if len(numbers) == 1:
        return numbers[0]

    largest = find_largest(numbers[1:])

    if numbers[0] > largest:
        return numbers[0]
    return largest


def count_number(numbers, target):
    if len(numbers) == 0:
        return 0

    if numbers[0] == target:
        return 1 + count_number(numbers[1:], target)

    return count_number(numbers[1:], target)


print("1. Sum the Array")
numbers = [10, 20, 30, 40, 50]
print("Array:", numbers)
print("Sum:", sum_array(numbers))

print("\n2. Find the Largest Number")
numbers = [12, 45, 23, 67, 34]
print("Array:", numbers)
print("Largest number:", find_largest(numbers))

print("\n3. Count a Chosen Number")
numbers = [5, 2, 5, 8, 5, 3, 5]
target = 5
print("Array:", numbers)
print("Target number:", target)
print("Count:", count_number(numbers, target))
