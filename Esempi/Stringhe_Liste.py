spam="Ciao mamma"
etc="Guarda come mi diverto"
es1=spam+etc            #concateno stringhe
es2=spam*3              #ripeto la stringa tre volte
print(es1)
print(es2)
#Lista
a=[1,2,4]
b=[4,5,6]
c=a+b                   #concateno liste
d=a*3                   #ripeto stringa
print(c)
print(d)

#lunghezza stringa e liste
print(len(d))
print(len(es1))

#verifico se esiste carattere interno stringa e lista
a=[1,2,3,4]
b="qwerty"
print(1 in a)       #carattere in lista
print("1" in b)     #carattere in stringa

#accedo elemento stringa
alfa = "abcdefghijklm..."

def reverser(stringa):
    indice = (len(stringa) -1)
    nuova_stringa = ""
    while indice >= 0:
        nuova_stringa += stringa[indice]
        indice -= 1
    print(nuova_stringa)

reverser(alfa)
#COnvertire Stringa il Lista, divido in lista con tutti caratteri stringa
beta=list(alfa)
print(beta)