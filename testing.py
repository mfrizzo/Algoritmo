# Brute Force

#Divisors of n 
def divisors(n_param):

    n = n_param
    divisors_list = []

    for num in range(1, n + 1):
        
        if n % num == 0:
            divisors_list.append(num)

    return divisors_list

n = 9647
result = divisors(n)
print('N: ' + str(n) + ' divisors: ' + str(result))

#Pin Unlock
from time import sleep 

def unlock(pin_param):

    pin = pin_param

    for i in range(10):

        for j in range (10):

            for k in range(10):

                for l in range (10):
                    guess = str(i) + str(j) + str(k) + str(l)
                    print(guess)
                    sleep(0.001)
                    if guess == pin:
                        # Pin unlocked
                        result = "El pin es: " + guess
                        return result
    return True

print(unlock('6743'))

#Sum of first n numbers
n = int(input("Ingrese n: "))
print("n: ", n)
suma = 0
for num in range(n + 1):
  suma = suma + num
print("Suma: ", suma)

# Lists

# Largest number in list
elements = [23, 45, 27, 4 ,89 ,8]
max = elements[0]
for i in range(len(elements)):
  if (elements[i] > max):
    max = elements[i]
print('Valor maximo: ', max)

#List merge
def juntar (list1, list2):
  newlist=[]
  x = 0 
  for i in range(len(list1)):

    if (list1[i] < list2[i]):

      if (list1[i] > x):

        x = list1[i]
        newlist.append(list1[i])
        x = list2[i]
        newlist.append(list2[i])

    elif (list2[i]< list1[i]):

      if (list2[i] > x):

        x = list2[i]
        newlist.append(list2[i])
        x = list1[i]
        newlist.append(list1[i])

  return newlist

#Recursion 

# Countdown
def countdown(n):
  print(n)
  if n == 0:
    return 0
  else:
    return countdown(n - 1)

#Factorial of n
def fact(n):
  if n == 0:
    return 1
  
  return (n * fact(n - 1))

print (fact(28))

#Fibonacci
import sys
sys.setrecursionlimit(2000)

def fib(n_param):
    n = n_param

    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(15))

# Sum of first n numbers recursion
import sys
sys.setrecursionlimit(2000)

def sum_of_n(n_param):
    n = n_param

    if n == 1:
        return 1
    
    else:
        return n + sum_of_n(n - 1)

print(sum_of_n(100))

# Searching

#binary search
def binary_search (list,search):

  inicio = 0
  final =  len(list)-1

  while inicio <= final:

    mitad = (inicio + final)//2

    if list [mitad] == search:
      return "Si se encuentra"

    elif list [mitad] < search:
      inicio = mitad + 1

    elif list [mitad] > search:
      final = mitad - 1
      
  return "No se encuentra"

# linear search
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

# Sorting

#bubble sort optimized
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

# bubble sort
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

# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        z = arr[i]
        j = i - 1

        while j >= 0 and z < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = z
    
    return arr

#selection sort
def selection_sort(arr):

    for i in range(len(arr)):

        min_i = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_i]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr

print(selection_sort([63, 16, -11, 13, 304, -2]))