######## SET ISTRUZIONI INTEGRATE- LIBRERIA STANDARD  ####

#Ciascun modulo è una funzione scritta da altri#

import random         #importato modulo random -> modo generale per importare

from math import sqrt #dal modulo math importo solo funzione radice quadrata


##### CRE0 10 NUMERI CASUALI TRA 1 E 50

for numero in range(10): #per 10 volte
    valore = random.randint(1, 50)  #genero numero casuale tra 1 a 50
    print(valore)

#calcolo radice quadrata

print(sqrt(125))  #avevo importato math

## USANDO from math import * importo tutti i moduli della funzione math
# Poi posso usare i moduli senza inserire math. davanti, come avevo fatto invece con random