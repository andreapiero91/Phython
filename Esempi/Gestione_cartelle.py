####### GESTIONE CARTELLE ######

import os
import shutil

#IN QUALE CARTELLA SONO?
print(os.getcwd())

#CONTENUTO CARTELLA AUTTUALE, TUTTO CONTENUTO
print(os.listdir())

#CAMBIO CARTELLA
os.chdir("C:\\") #dico voglio spostarmi in C:\\
print(os.getcwd())

#CREO CARTELLA CON QUESTO NOME
os.makedirs("C:\\n__cartella")

#RINOMINO CARTELLA (nome attuale, nuovo nome)
os.rename("n__cartella","lezione_21")
print(os.listdir())

#SPOSTARE CARTELLA
#shutil.move("C:\\lezione_21\\security","c:\\lezione_21\\informatica")

#COPIA CREANDO NUOVA CARTELLA, copio anche sottocartelle
shutil.copytree("C:\\lezione20","C:\\lezione21\\lezione20copia")


################NAVIGARE FILE SYSTEM#########

#Voglio separare quando vedo cartelle,sottocartelle,files
os.chdir("C:\\lezione20")
#ogni ciclo entra in sottocartella della cartella dove sono
for cartella, sottocartelle, files in os.walk(os.getcwd()):
    print(f"Ci troviamo nella cartella: '{cartella}'")
    print(f"Le sottocartelle presenti sono: '{sottocartelle}'")
    for file in files:  #tralascio file che non sono python
        if file.endswith(".py"):
            print(file)
    print()