#### PROGRAMMAZIONE A OGGETTI: classi e Istanze

class Studente:              #defininosco una classe
    ore_settimanali= 36      #VARIABILI DI CLASSE, si applicano a tutti gli oggetti di quella classe
    numero_studenti=0

    def __init__(self,nome,cognome,corso):  #COSTRUTTORE
        self.nome=nome                      #ciascun singolo oggetto creato
        self.cognome=cognome
        self.corso=corso
        Studente.numero_studenti+=1         #per ogni studente, aumento il numero degli studenti presenti

    @staticmethod                       #METODO STATICO, non si applica a nessun oggetto in particolare
    def info_prog():                    #posso richiamarlo con nomeclasse.metodo
        info = """
            Nome: Persona
            Creato da: PyMike
            Portale: www.programmareinpython.it
            Commenti: Scritto usando Python 3.6"""

        return info

    def scheda_personale(self):                 #come TOSTRING() in java
        return f"Scheda Studente\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso Di Studi:{self.corso}\n Ore Settimanali:{Studente.ore_settimanali}"


studente_uno = Studente("A","B","phyton")               #Costruisco oggetto studente
studente_due = Studente("marco","pala","peneGrosso")

studente_uno.ore_settimanali+=4                         #aggiorno solo le ore settimanali dello studente uno


print(studente_uno)                                     #RESTITUISCE ALLOCAZIONE MEMORIA
print(studente_due)

print(studente_due.scheda_personale())                  #Dati dello studente

print(Studente.scheda_personale(studente_uno))          #Altro modo per aver i Dati dello studnete

print(Studente.numero_studenti)                         #sarà pari a 2

print(Studente.info_prog())

