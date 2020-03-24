###### DIZIONARIO ######
#Come liste, ma ad ogni valore ho indice particolare chiamato chiave
#la chiave può essere tutto tranne una lista o un dizionario
#ho coppie [chiave:valore]

mio_dizionario ={"mia_chiave_uno":"mia_chiave_due","eta":24,3.14:"pi","primi":[1,3,5]}

#Uso chiave per richiamare elemento associato a chiave (indico chiave)

print(mio_dizionario[3.14])

#Aggiungere elemento al Dizionario
mio_dizionario["nuova_chiave"]="new_valore"

#sostituisco valore nel dizionario
mio_dizionario["eta"] = 99  #ora salvo nell'elemento con chiave eta
print(mio_dizionario)       #il valore 99

#Due DIZIONARI SONO UGUALI se contengono stesse copie chiave valore anche
#se non sono nello stesso ordine

#Chiave è presente nel dizionario? Se si, True

print("primi" in mio_dizionario)

#Eliminare coppia-chiave-valore

del mio_dizionario["mia_chiave_uno"] #Dico di eliminare coppia con chiave mia_chiave_uno
print(mio_dizionario)

######## ESEMPIO2  ######

ita_eng= {"ciao":"hello","uova":"eggs","gatto":"cat"}

#METODO KEYS: lista tutte chiavi presenti
print(ita_eng.keys())

#METODO VALUES: elenco tutti i valori
print(ita_eng.values())

#METODO ITEMS: coppia chiave:valore
print(ita_eng.items())

#LISTA tutte parole inglese
parole_eng = list(ita_eng.values())

#ciclo su tutte chiavi dizionario
for chiave in ita_eng.keys():
    print(chiave)

#ERRORE se uso chiave non presente, Keyerror

print(ita_eng.get("ciao","Chiave non trovata")) #Se trova ciao nelle chiavi
#mi da il valore, altrimenti mi stampa Chiave non trovata

#Se non ce, la voglio aggiungere
ita_eng.setdefault("birra","beer") #Se non la trovo, copia birra:beer

print(ita_eng)