def selection_sort(arr):

    for i in range(len(arr)):

        min_i = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_i]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr

print(selection_sort([63, 16, -11, 13, 304, -2]))