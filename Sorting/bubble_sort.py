def bubble_sort_opt(arr):

    for i in range(len(arr)):

        is_sorted = True

        for j in range(len(arr) -i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
    
        if is_sorted:

            return arr

    return arr

print(bubble_sort_opt([98, -14, 72, 2, 13, -54]))