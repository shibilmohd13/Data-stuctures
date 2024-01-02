def quicksort(arr, left, right):
    if left < right:
        partition_index = partition(arr, left, right)
        quicksort(arr, left, partition_index - 1)
        quicksort(arr, partition_index + 1 , right)

def partition(arr, left, right):
    i = left 
    j = right - 1
    pivot = arr[right]

    while i < j:
        
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]

    if arr[i] > pivot:
        arr[i] , arr[right] = arr[right] , arr[i]

    return i


my_list = [3, 6, 8, 10, 1, 2, 1]

quicksort(my_list, 0, len(my_list)-1)

print(my_list)