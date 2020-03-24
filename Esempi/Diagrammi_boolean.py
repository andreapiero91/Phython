#BOOLEAN
#Definisco con True False

import math
import geopandas
Cancello= True   #Assegno valore T, F

#Comparazione con True e False
print(23<50)     #Stampo True

# E.S. 33 == "33" false, "33" è in stringa

######  OPERATORI BOOLEANI  ######
#Quelli ben noti and, or, not

######### IF #######
#RICORDA IDENTAZIONE

eta= 19           #verifico se posso guidare
Patente= False


if eta >= 18 and Patente == True:   #caso if
    print("Sei maggiorenne e puoi noleggiare una ferrari") #devo mettere spazio all'inizio riga(tab)
elif eta >=18 and Patente == False: #caso elsif
    print("Sei maggiorenne ma non puoi noleggiare la ferrari")
else:
    print("Sei minorenne")    #N.B. Else Sempre ultimo ad essere eseguito

####### CICLO WHILE ########

contatore=0

while contatore<=10:  #finchè contatore <10, eseguo operazioni
    print(contatore)         #stampo contatore
    contatore = contatore+1  #incremento


######### BREAK  #########

contatore = 0
while True:             #CICLO  infinito
    print(contatore)
    contatore += 1
    if contatore > 10:  #Quando arrivo > 10
        print('Sto uscendo dal loop!')
        break                           #se contatore >10, esco dal ciclo while

######### CONTINUE ##########

    contatore = 0
    while contatore < 10:
        contatore += 1
        if contatore == 3: #Se contatore è pari a 3, scrivo saltato e..
            print('saltato') #passo al prossimo giro del ciclo, non stampo contatore
            continue
        print(contatore)


####### FOR E RANGE  #########

for numero in range(11):  #punto inizio,  dove arrivo(escluso), di quanti numeri  salto
    print(numero)         #di default parto da 0

for numero in range(3,11,2):  #parto da 3, fino a max 11 escluso, saltando 2 numeri
    print(numero)             #stampo 3 5 7 9
