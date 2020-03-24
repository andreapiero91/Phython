#####       ANALISI ARGOMENTI E OPZIONI LINEA DI COMANDO #####

import argparse

def calcolatrice(n1, n2, operazione):   #Semplice calcolatrice
    if operazione == "add":
        return n1 + n2
    elif operazione == "sot":
         return n1 - n2
    elif operazione == "mol":
        return n1 * n2
    elif operazione == "div":
        return n1 / n2

#Oggetto tipo ArgomentParser

#descrizione della funzione
parser = argparse.ArgumentParser(description="Semplice Calcolatrice per addizioni, sottrazioni, moltiplicazioni e divisioni")
#richiamandolo con -h, crea lui funzione help molto utile

#PARAMETRI LINEA COMANDO, nome; tipo; descrizione in help -> di default sono stringhe
parser.add_argument("n1", type=float, help="Primo Numero")
parser.add_argument("n2", type=float, help="Secondo Numero")
parser.add_argument("operazione", type=str, help="Tipo di operazione",choices = ["add", "sot", "mol", "div"])
#con choses indico i valori accettati, se digita altro stampo messaggio errore

#PARAMETRI OPZIONALI  -> azione default store_true, deposito valore true in variabile quiet se viene passato
#voglio che siano mutui esclusivi, o digito verbose o quite

group = parser.add_mutually_exclusive_group() #Gli argomenti in group sono mutuamente esclusivi, o digito un'opzione o digito l'altra
group.add_argument("-v", "--verbose", help="Restituisce output verboso.", type=int, choices=[1,2]) #Posso digitare -v 1 oppure -v 2
group.add_argument("-q", "--quiet", help="Output non verboso", action="store_true")
args= parser.parse_args()

risultato= calcolatrice(args.n1,args.n2,args.operazione)

if args.quiet:  #Se ho scelto -q
    print(risultato)
elif args.verbose == 1: #se ho scelto -v 1
    print(f"Il risultato dell'operazione '{args.operazione}' è: {risultato}")
elif args.verbose == 2:
    print("Benvenuti al programma Calcolatrice!")
    print(f"Il risultato dell'operazione '{args.operazione}' tra '{args.n1}' e '{args.n2}' è: {risultato}")
else:
    print(f"Il risultato dell'operazione è: {risultato}")