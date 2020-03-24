x=15 #globale, dichiarata fuori funzione -> creata all'avvio

def funzione_esempio(): #all'interno ho ambito locale
    global x            #dico a phyton che sto usando la variabile globale che si chiama x
    x+=2
    return(x)           #ritorno 17

def funzione_esempio2(): #Funziona uguale
    y = x                #ora y vale 17, assegno a x il valore della variabile globale x (si può fare)
    y += 2
    return(y)           #ritorno 19

print(funzione_esempio())
print(funzione_esempio2())