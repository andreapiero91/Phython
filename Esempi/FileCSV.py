#### CARATTERE DELIMITATORE PUO' ESSERE QUALUNQUE ####
import  csv

#apro come file csv
with open("Mappa-fermate-autobus-in-Italia.csv", newline="", encoding="ISO-8859-1") as filecsv:
    lettore=csv.reader(filecsv,delimiter=";") #leggo riga per riga
    header=next(lettore)                      #intestazione documento
    print(header)

    #In dati salvo il quarto(3) elemento della linea
    #Solo se il primo elemento(0) è Agliè
    dati = [(linea[3]) for linea in lettore if linea[0]=="Aglie'" ]
    print(dati)