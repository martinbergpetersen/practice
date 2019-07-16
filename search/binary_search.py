def binary_search(numbers, key):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            return True, key
    return False, None


search = range(1000000000000000000)
print(binary_search(search, 100000000000000))
