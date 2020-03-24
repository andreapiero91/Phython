####            EREDITA'       ####

#Classe base
class Persona:

    def __init__(self, nome, cognome, età, residenza):  #Costruttore
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    def scheda_personale(self):                         #toString
        scheda = f"""
        Nome: {self.nome} 
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda

    def modifica_scheda(self):                           #modifica dati Persona
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")
        scelta = input("Cosa Desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome--> ")
        elif scelta == "2":
            self. cognome = input("Nuovo Cognome --> ")
        elif scelta == "3":
            self.età = int(input("Nuova età --> "))
        elif scelta == "4":
            self.residenza = input("Nuova Residenza --> ")
        else:
            print("Scelta errata")

class Studente(Persona):    #Cosa modifico rispetto a Persona? (Persona) significa eredita da Persona
    profilo="Studente"      #ATTRIBUTO solo della classe Studente

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):  ### COSTRUTTORE STUDENTE
        super().__init__(nome, cognome, età, residenza)                  #Costruttore padre
        self.corso_di_studio = corso_di_studio                           #Studente ha in più il CORSO DI STUDIO

    def scheda_personale(self):                                         #SOVRASCRIVO metodo genitore to String
        scheda = f"""
        Profilo:{Studente.profilo}
        Corso di Studi:{self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda

    def cambio_corso(self, corso):                                      #Modifico cambio corso di studio
        self.corso_di_studio = corso
        print(f"Corso Aggiornato")
        
    pass

class Insegnante(Persona):
    profilo = "Insegnante"
    pass

studente_uno = Studente("Py", "Mike", 24, "Casa Dello Studente","Ingegneria Informatica")
insegnante_uno = Insegnante("Mario", "Rossi", 33, "Viale Roma 32")

print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale()) #Richiama il metodo sceda_personale presente in  Persona
                                         #se non trova un metodo in Studente, lo cerca nel genitore Persona

######## METODO HELP ######

#print(help(Studente))  ## Mi da informazioni su cosa eredità, da chi ecc

