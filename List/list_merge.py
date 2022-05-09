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
