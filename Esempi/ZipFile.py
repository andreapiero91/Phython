##### FILE ZIP #####

import os
import zipfile  #occupa compressione e decompressione

#CREAZIONE NUOVO ARICHIVIO

# creazione/apertura in modalità scrittura (nome zip file, modalità scrittura)
archivio = zipfile.ZipFile('mio_archivio.zip', "w")

# aggiunta file e compressione -> deflated is algoritmo di compressione
archivio.write("Calcolatrice.py", compress_type=zipfile.ZIP_DEFLATED)

archivio.close() #ricordati di chiudere sempre gli archivi

#N.B. OPZIONE W CANCELLA FILE CHE GIA' ERANO DENTRO ARCHIVIO

# apertura in MODALITA' AGGIUNTA-> no cancello cosa ce già dentro archivio

archivio = zipfile.ZipFile('mio_archivio.zip', "a")  #(nome_archivio, modalità)

archivio.write("Dizionario.py", compress_type=zipfile.ZIP_DEFLATED)

archivio.close()

#ESTRAGGO FILE DA ARCHIVIO

archivio = zipfile.ZipFile("mio_archivio.zip") #quale archivio voglio leggere
archivio.extractall()                          #inserisco interno() percorso dove estrarre

#exctract() è la funzione per estrarre un solo file, indico quale

#QUALI SONO I FILE PRESENTI NELL'ARCHIVIO
a=archivio.namelist()
print(a)

#INFORMAZIONI SU FILE
urlsinfo = archivio.getinfo("Dizionario.py") #di quale file in archivio voglio info
b=urlsinfo.file_size  #dimensione originale
c=urlsinfo.compress_size #dimensione compressa
print(b)
print(c)

archivio.close()