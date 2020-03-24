########## LISTA ########
# Def: Insieme dati uguali o diverse

elenco = [2,5,"bacon",3.14,"eggs"] #creo lista con parentesi quadre

print(elenco) #stampo la lista

#accedere al terzo elemento(bacon), l'indice parte da zero
print(elenco[2])

#usando indice negativo, accendo elementi partendo dall'ultimo(-1)
print(elenco[-2])   #in posizione -2, partendo da -1 ho 3.14

######## ACCESSO A PIU' ELEMENTI #####
primi = [2,3,5,7,11,13,17,19,23,29]

print(primi[3:9]) #creo nuova lista, con elementi da 3 a 9
                  #ricordando che parto da zero

print(primi[5:]) #elementi da 5 a ultimo(ricorda indice parte da 0)

####STAMPO TUTTI ELEMENTI LISTA uno dopo l'altro, collocando ogni singolo elemeto dentro var primo
for primo in primi:
    print(primo)

 #RANGE PER TUTTI I NUMERI tra x e y
#creo lista con tutti elementi tra 99 e 300

lista_numerica = list(range(99,300)) #300 non incluso
print(lista_numerica)

#LISTA MULTIPLA, OVVERO LISTA DENTRO LISTA

lista_multipla = ["spam", "egg",23,"bacon",[1,2,3],3]

print(lista_multipla[-2][2]) #terzo (secondo) elemento del secondo elemento da dx
                             #stampo 3
##### MODIFICARE UNA LISTA

lista_multipla[3]="pancetta" #cambio bacon in pancetta
print(lista_multipla)

del lista_multipla[-2]   #elimino secondo elemento dal fondo, ovvero lista interna
print(lista_multipla)

##### TUPLE: NON SONO MODIFICABILI!! #######

tuple1 =(7,8,9) #due modi per creare tuple
tuple2 = 4,5,6

######### METODI PER LE LISTE ########

inventario = ["torcia","spada","arco","pane elfico"]

#aggiungo elemento in coda
inventario.append("frecce")
print(inventario)


def riempi_inventario():  #riempio lista inventario
    inventario = []
    oggetto = ""          #oggetto vuoto
    while True:           #ciclo infinito
        oggetto = input('Cosa vuoi aggiungere all\'inventario? ')
        if oggetto == "terminato":   #caso terminazione
            break
        else:
            inventario.append(oggetto)

print("Gli oggetto presenti nell'inventario sono: " + str(inventario))


riempi_inventario()

#elemino elemento da lista passando valore

monty=[1,2,34,5,6,7]
monty.remove(34) #voglio eliminare l'elemento 34
print(monty)

#ordinare elementi nella lista

alfabeto=["z","a","w"]
alfabeto.sort()         #stringhe, ordino maniera lessicografica
print(alfabeto)
                           #sort(reverse=True) ordina in ordine da ultimo a primo

#in che indice è il dato che passo?

print(alfabeto.index("z")) #dove è z?

#Inserisco nella posizione che indico

alfabeto.insert(1,"b") #Inserisco b in seconda posizione
print(alfabeto)