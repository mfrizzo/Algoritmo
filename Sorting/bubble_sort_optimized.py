array = [2, 4, 0, 1, 9, 5]
x = 1
y = len(array)

def linearSearch (array, y, x):

  for i in range (0, y):
    if (array[i] == x):
        return i
    return -1

result = linearSearch(array, y, x)

if (result == -1):
    print("Error")
else:
    print("Elemento: ", result)