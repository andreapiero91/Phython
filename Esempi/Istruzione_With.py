####### ISTRUZIONE WITH #####
#Risparmio riga chiusura file

with open("zaza.txt","r") as zenigata: #with pensera a chiudere file alla fine
    for riga in zenigata:
        print(riga)

print(zenigata.closed)  #True se file chiuso

#N.B. usando le eccezioni, potrò non mettere in finally la chiusura del file -> già chiuso
