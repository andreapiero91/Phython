import shutil
import os

shutil.copy("C:\\lezione20\\1492.txt","C:\\lezione20\\storia")
#copio file da sorgente a destinazione (src, dst)

shutil.move("C:\\lezione20\\napoleone.txt", "C:\\lezione20\\storia")
#sposto file dentro cartella storia

os.unlink("C:\\lezione20\\cancellami.txt")
#elimina file da hard disk

#rinomina file
os.rename("C:\\lezione20\\rinominami.txt", "file_rinominato.txt")

