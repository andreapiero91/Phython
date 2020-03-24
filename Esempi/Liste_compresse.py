
########## LISTE COMPRESSE #########

quadrati=[]                     #Lista con i quadrati dei numero da 0 a 9
for n in range(10):
    quadrati.append(n**2)

print(quadrati)

##STESSO RISULTATO CON LIST COMPRESSIONE

quadrati=[n**2 for n in range(10)] #scrittura accorciata
print(quadrati)

###       ES2   ###
#Creo coppie di numeri (a,b) se a diverso da b
lista1=[1,2,3]
lista2=[3,1,4]

mix=[]
for x in lista1:
    for y in lista2:
        if x!= y:
            mix.append((x,y)) #creo la coppia

print(mix)

######### Riscrivo in maniera compatta

mix=[(x,y) for x in lista1 for y in lista2 if x!=y]
print(mix)

##### ES 3, CONVERTO da lista a stringa

stringati=[str(n) for n in lista1]
print(stringati)