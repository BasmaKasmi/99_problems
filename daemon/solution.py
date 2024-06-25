# Define the function
def daemon(numbers, k):
    if k < 0 or k >= len(numbers):
        return False

    pivot = numbers[k]

    for i in range(k):
        if numbers[i] >= pivot:
            return False

    for i in range(k + 1, len(numbers)):
        if numbers[i] < pivot:
            return False

    return True

