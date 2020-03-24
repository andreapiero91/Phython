### METODI CHE PHYTON  CHIAMA PER NOI IN DETERMINATE CIRCOSTANZE ###

#ES 1 - DIZIONARIO CON LETTERA:POSIZIONE

alfabeto = {1: "a", 2: "b", 3: "c", 4: "d"}

print(type(alfabeto)) #Restituisce il tipo -> dict
                      #Phyton chiama per noi un metodo interno che compie questa operazione

#anche con alfabeto[4], phyton all'interno chiama metodo  __getitem__

# help(alfabeto)  #ELENCO DI TUTTI I METODI DUNDER

###### ES.2  CON CLASSE   #######

class Studente:
    # Una semplice classe Studente

    def __init__(self, nome, cognome, corso_di_studi):  #Costruttore
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi


    def scheda_personale(self):     #toString
        return f"""
            Scheda Studente \n
            Nome: {self.nome}
            Cognome: {self.cognome}
            Corso Di Studi: {self.corso_di_studi}
            """

    def __add__(self, other):    #Sono metodi standard, già presenti per i dati standard, come int
                                 #Posso ridefinire come voglio io, per le mie classi
        # Solo per fini didattici. Usare i dunder in maniera intelligente! #
        return self.nome + " " + other.cognome  #ridefinisco operatore +

    def __str__(self):      #Personalizzo, rappresentazione leggibile
        return f"Lo Studente {self.nome} {self.cognome}"

    def __repr__(self):       #Esaustivo e non ambiguo, per sviluppatori-> output più corposo(nel dubbio meglio questo di str)
        return f"Studente('{self.nome}', '{self.cognome}', '{self.corso_di_studi}')"


studente_uno = Studente("Peter", "Malkovich", "Psicologia")         #creo Studente
studente_due = Studente("John", "Snow", "Antropologia")

print(studente_due + studente_uno)

#Cosa capita se passo a print o a str la calsse studente? #da di default indirizzo memoria, inutile per studente

print(studente_uno)

print(str(studente_due)) #Restituisce stesso formato di solo print

print(repr(studente_due))#Formato esteso