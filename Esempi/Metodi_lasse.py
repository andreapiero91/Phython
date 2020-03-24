class Persona:

    def __init__(self, nome, cognome, età, residenza):          #COSTRUTTORE
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    @classmethod                                   #permette alterare comportamento metodi ->DECORATORE METODI DI CLASSE
    def from_string(cls,stringa_persona,*args):  #passo come primo parametro la classe stessa, non la singola istanza; poi la stringa voglio separare
        nome, cognome, età, residenza = stringa_persona.split("-") # *args se ho dei parametri in più
        return cls(nome, cognome, età, residenza,*args) #args si usa se posso avere più parametri senza sapere quanti, nelal classi figlie
        pass    #from_string è una convenzione

    @classmethod        #cambia funzionamento a seconda di su quale sottoclasse è applicato
    def occupazione(cls):
        if (cls.__name__ == "Studente"):
            return "Studente"
        else:
            return "Insegnante"

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome} 
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")

        scelta = input("Cosa Desideri Modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome --> ")
        if scelta == "2":
            self.cognome = input("Nuovo cognome --> ")
        if scelta == "3":
            self.età = input("Nuovo età --> ")
        if scelta == "4":
            self.residenza = input("Nuovo residenza --> ")


class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Studente.profilo}
        Corso Di Studi:{self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda

    def cambio_corso(self, corso):
        self.corso_di_studio = corso
        print("Corso Aggiornato")


class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self, nome, cognome, età, residenza, materie=None): #di default è pari a None
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Insegnante.profilo}
        Materie Insegnate:{self.materie}
        ***"""
        return super().scheda_personale() + scheda



#### COSTRUTTORE ALTERNATIVO __INIT __

iron_man = "Tony-Stark-40-Torre Stark" #preleva dati da stringa, come se fossero su un file
PazzoLazzo ="Mario-Catarro-45-Via le mani dal naso"

persona1=Persona.from_string(iron_man)
stud1=Studente.from_string(PazzoLazzo,"O.S") #con args gestisco il paramentro in più che è Corso

#insegnante1=Insegnante.from_string(PazzoLazzo,"O.S")
print(persona1.scheda_personale())
print(stud1.scheda_personale())
#print(insegnante1.scheda_personale())