def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left_arr, right_arr):
    sorted_arr = []
    while left_arr and right_arr:
        if left_arr[0] <= right_arr[0]:
            sorted_arr.append(left_arr.pop(0))
        else:
            sorted_arr.append(right_arr.pop(0))

    result_arr = sorted_arr + left_arr + right_arr
    
    return result_arr

arr = [64, 34, 25, 12, 22, 11, 90]
merge_sorted_array = merge_sort(arr)
print("Merge Sorted array:", merge_sorted_array)
