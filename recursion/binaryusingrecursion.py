def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target element found, return its index
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1  # Target element not found

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = binary_search_recursive(sorted_array, target_element, 0, len(sorted_array) - 1)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")
