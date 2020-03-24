######## LINEA COMANDO ########

import sys

#print(sys.argv)

if len(sys.argv) <3:
    print("Devi passare due paramentri allo script!")
    print("Sto uscendo")
    sys.exit()

nome_script, primo,secondo=sys.argv

print(f"""
Il nome dello script è: {nome_script}
Il primo parametro passato è: {primo}
Il secondo parametro passato è: {secondo}""")