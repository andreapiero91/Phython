import camelcase
import numpy as np
import pandas

c = camelcase.CamelCase()

txt= "lorem ipsum dolor sit amet"

print(c.hump(txt))

####### NUNPAY  #####

arr1 = np.array([1, 2, 3, 4, 5])  #creo semplice array -> posso passare lista tupla o qualsiasi altro arrray-like object

print(arr1)

arr = np.array([[1, 2, 3], [4, 5, 6]]) #2D ARRAY

print(arr)

#Dimensione dell'array

print(arr.ndim)

#ACCESSO A UN ELEMENTO -> l'array inizia con 0; posso iniziare con indice -1 dal fondo
print(arr1[0])

print('2nd element on 1st dim: ', arr[0, 1])   #Primo sottovettore, Secondo elemento(1)


#SLICING:accedo elementi da x a y saltando z [x,y,z]
print(arr1[1:4:2])  #parto da 1, a 4 saltando ogni 2

#COPIA E VIEW
#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

print("*****************************")
#Shape of an Array Iis the number of elementi in each dimension
print(arr.shape)  #2,3 poichè ha due dimensioni, ognuna delle quali ha 4 elementi

print("*********************************")

#CICLO SU ELEMENTI DEL VETTORE


for x in arr:   #È MATRICE, STAMPA LE DUE RIGHE SEPARATE
  print(x)

for x in arr:    #elemento per elemento
  for y in x:
    print(y)

#CONCATENARE DUE ARRAY N.B. Esistono altre modalità di concatenazione, per le matrici, vedi su W3C

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

#SPLIT: split array in sottoaaray

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

print("********************")
###### METODI ####

###SEARCH ###

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)  #In che posizione ho valore 4? in pos3, pos5 e pos6

print(x)

###SORT ###
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))   #ordino in modo crescente

print("***********************")
##FILTERING: si fa con True negli elementi voglio tenere, False voglio eliminare

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

##SECONDO MODO, solo elementi dispari


arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)