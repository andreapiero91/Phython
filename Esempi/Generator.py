## GENERATORs E YIELD ##

def countdown():        #GENERATOR FUNCTION, creo contatore all'indietro
    i = 5
    while i > 0:
        yield i         #Ritorna, MANTENENDO ALL'INTERNO LO STATO DELLE VARIABILI
        i -= 1


for i in countdown(): #Quando rientro nella funzione, salto al comando dopo l'ultimo yield che aveva ritornato
    print(i)

#NB SE GENERO tutta una serie di numeri, come quelli da mettere in una lista, occupo meno memoria poichè
#li genero uno alla volta(nel ciclo for) e li ritorno con yield uno alla volta