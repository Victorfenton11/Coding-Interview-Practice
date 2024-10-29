def merge(arr, left, mid, right):
    l1 = mid - left + 1
    l2 = right - mid

    leftarr = [0] * l1
    rightarr = [0] * l2

    for i in range(l1):
        leftarr[i] = arr[left + i]
    for j in range(l2):
        rightarr[j] = arr[mid + j + 1]
    
    i, j, k = 0, 0, left
    while i < l1 and j < l2:
        if leftarr[i] <= rightarr[j]:
            arr[k] = leftarr[i]
            i += 1
        else:
            arr[k] = rightarr[j]
            j += 1
        k += 1
    
    while i < l1:
        arr[k] = leftarr[i]
        i += 1
        k += 1
    
    while j < l2:
        arr[k] = rightarr[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

arr = [9, 8, 5, 3, 6, 2, 4, 6]
merge_sort(arr, 0, len(arr) - 1)
print(arr)