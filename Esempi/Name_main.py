###        FUNZIONE MAIN     ###

def main():         #Come se fosse funzione principale in c
    print("Prime righe voglio eseguire, se a __name__ contiene __main__")
    print(__name__)


def stampa_lambda():
    print("lambda")


if __name__ == "__main__":  #permette capire se eseguito come script a se stante
    main()                  #o se viene chiamato da altri script

#Tra le prime cose che phyton fa, assegna alcuni valori, come ad esempio la variabile name
#Se si rende conto che lo sta eseguendo direttamente come script, digitando ad esempio
#tramite Pycharm/shell, assegno alla variabile  name il valore __main__

##Richiamo quindi la funione main, che contiene le prime righe che voglio eseguire

##Se richiamo da esterno, altro file, avrò in __name__ il nome del file
##(Vedi cosa succede chiamando la funzione f(stampa lambda) dal file Name_main_prova)