def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less = [x for x in arr[:-1] if x <= pivot]        
        greater = [x for x in arr[:-1] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

arr = [64, 34, 25, 12, 22, 11, 90]
quicksort(arr)
print("Selection Sorted array:", arr)
