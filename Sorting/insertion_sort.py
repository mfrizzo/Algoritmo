def insertion_sort(arr):
    for i in range(1, len(arr)):
        z = arr[i]
        j = i - 1

        while j >= 0 and z < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = z
    
    return arr