### CONCATENAZIONE TESTO VARIABILI ###

#FINO ORA
nome="jack"
print("ciao"+nome)
numero=18
print("Ciao "+nome+" hai "+ str(numero) + " anni")

####NUOVO METODO, f sta per formattazione e {variabile} #####

saluto= f"Ciao {nome},hai {numero} anni"
print(saluto)

#Es2
z=5
q=f"Il quadrato di {z} è {z *z}"
print(q)

###### METODI DA APPLICARE ALLE STRINGHE"
messaggio="fate il vostro gioco"

#starstwith -> ritorna True se inizia con ()
print(messaggio.startswith("fate"))
print(messaggio.startswith("x"))

#endswith -> ritorna True se finisce con cosa indicato in ()

print(messaggio.endswith("jock"))

#isupper e islower, restituiscono True se tutte maisucole o tutte minuscole

# lower e upper convertono in tutti caratteri maiuscoli e tutti minuscoli

#isaplha is True se stringa tutta maiuscola(N.B. anche uno spazio da Falso)

#isdecimal is True se stringa formata da soli numeri

#isalnum is True se formata da lettere e numeri


#### METODO JOIN ####   LISTA -> STRINGA

compiti = ["cane a passeggio", "finire studiare","lavare i panni"] #creo lista con elementi

#Chiamo su lista indicando (cosa voglio come separatore nella stringa).join(lista voglio unire)
da_fare = "oggi devo " + ", ".join(compiti)
print(da_fare)

#es2
d_fare= "\n".join(compiti) #metto a capo come separatore, vado a capo ogni riga
print(d_fare)

######## SPLIT ##### STRINGA CON SEPARATORE -> LISTA

serie_numerica = "1492-1978-156-1345" #separatore -

print(serie_numerica.split("-")) #metto in lista, indicando quale è separatore
#uso carattere - come separatore (potrei usare anche spazio)