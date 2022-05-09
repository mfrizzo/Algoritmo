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