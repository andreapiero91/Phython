##FUNZIONI UTILI

from itertools import count,accumulate

#COUNT
for i in count(3):  #Conta infinite Volte a partire da 3
  print(i)
  if i >=11:
    break

#ACCUMULATE: somma numeri
nums = list(accumulate(range(8)))  #Sommo i primi 8 numeri e li metto in una lista [0 1 3 6 10...]
print(nums)