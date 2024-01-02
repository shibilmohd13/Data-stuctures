def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    sorted_array = []
    while left and right:
        if left[0] <= right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))

    result_array = sorted_array + left + right
    return result_array


arr = [64, 34, 25, 12, 22, 11, 90]
merge_sorted_array = merge_sort(arr)
print("Merge Sorted array:", merge_sorted_array)        