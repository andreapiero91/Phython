############## FUNZIONI ##############
##definita con def

def print_tre_volte():  #def definisce la funzione
    print("Ciao")       #metto i parametri che gli vengono passati tra ()
    print("Come va")
    print("io sto bene e tu")

def sommatrice(a,b):    #esegue la somma
    print("Questa è la funzione somma")
    print("Fornisce la somma di due parametri ")
    somma=a+b
    return somma        #ritorno il valore della somma

print_tre_volte()
print(sommatrice(3,5))

##### PARAMETRI DEFAULT #####
# Se non indico il paramentro, sarà quello indicato in intestazione

def laptop(ram,cpu,antivirus=False): # antivirus avrà False di default
    print("Il nuovo laptop avrà")
    print(ram)
    print(cpu)
    if antivirus == True:            #Se il parametro è true, stampo
        print("Hai comprato l'antivirus") #Altrimenti non hai comprato l'antivirua


laptop("16gB","i7") #posso chiamare così, prenderà di default false
laptop("16gB","i7",True)