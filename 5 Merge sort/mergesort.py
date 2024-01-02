def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)


        i = 0  # left_arr index
        j = 0  # right_arr index
        k = 0  # Merged arr index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Check if there are any remaining elements in right_arr
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]

# Call the merge_sort function to sort the array in-place
merge_sort(arr)

# Print the sorted array
print("Merge Sorted array:", arr)
