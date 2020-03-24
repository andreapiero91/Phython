##TRY, PARTE ESEGUO SE VA TUTTO BENE
##EXCEPT, PARTE ESEGUO SE SCATENATA ECCEZZIONE

def divisore(a,b):
    try:                #se tutto va bene, continuo qui ed eseguo tutto: se qualcosa scatena eccezione, passo a except
        risultato =a/b
        print("Il risultato è "+ str(risultato))
    except ZeroDivisionError:           #se si genera errore (poichè divido per zero), lo gestisco qui
        print("ERRORE: hai diviso per zero")
    finally:                             #eseguito sempre, sia se tutto è andato bene sia ho scatenato eccezione
        print("grazie di avere usato questa funzione")

divisore(4,5)
divisore(3,0) #genero eccezione