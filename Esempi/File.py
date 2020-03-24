### WRITE: cosa c'era nel file, elimino se stesso nome ###
### APPEND: accodo al file se ce già ###

contenuto="oggi è una bellissima giornata"

file1= open("esempio1.txt","w") #apro file in scrittura
#nome file e modalità scrittura
#salva in Pcharmprojects/Esempi

file1.write(contenuto) #scrivo
file1.close()

### APPEND ###
nuova_stringa = "python è una bomba"

file1=open("esempio1.txt","a")#modalità append, scrivo dopo cosa c'era già
file1.write("\n")
file1.write(nuova_stringa)
file1.close()

##READ
#salvo in var_lettura il testo
var_lettura= open("esempio1.txt","r").read()
print(var_lettura)

#Lettura riga per per riga -> readlines, inserisco in lista

var_lettur= open("esempio1.txt","r").readlines()
print(var_lettur)

######IMPORT OS
import os
print(os.getcwd()) #in che cartella sono
os.chdir("C:\\")   #mi sposto
print(os.getcwd())