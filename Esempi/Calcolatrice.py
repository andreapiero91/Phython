
while True:             #CICLO INFINITO
    print('''    
    Benvenuto al programma calcolatrice!
    Creata da: Andrea
    Di seguito un elenco delle varie funzioni disponibili:

    -Per effettuare un'Addizione, seleziona 1;
    -Per effettuare una Sottrazione, seleziona 2;
    -Per effettuare una Moltiplicazione, seleziona 3;
    -Per effettuare una Divisone, seleziona 4;
    -Per effettuare un Calcolo Esponenziale, seleziona 5;
    -Per uscire dal programma puoi digitare ESC;
    ''')  #PRINT MULTIRIGA, USO TRE APICI

    scelta = input('Inserisci il numero corrispondente all\'operazione selezionata --->  ')  #Inserisce valore l' utente

    if scelta == "1":
        print('\nHai scelto: Addizione\n')
        a = float(input('Inserisci il Primo Numero -> ')) #voglio che il dato inserito sia collocato in un float
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato della Somma è: ' + str(a + b)) #converto in stringa risultato di a+b
    elif scelta == "2":
        print('\nHai Scelto: Sottrazione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato della Sottrazione è: ' + str(a - b))
    elif scelta == "3":
        print('\nHai scelto: Moltiplicazione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato della Moltiplicazione è: ' + str(a * b))
    elif scelta == "4":
        print('\nHai scelto: Divisione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato della Divisione è: ' + str(a / b))
    elif scelta == "5":
        print('\nHai scelto: Calcolo Esponenziale\n')
        a = float(input('Inserisci la Base -> '))
        b = float(input('Inserisci l\'Esponente -> '))
        print('Il risultato del Calcolo Esponenziale è: ' + str(a ** b))
    elif scelta == "ESC":                   #ESC -> esco dal ciclo
        print('''L'applicazione verrà ora chiusa!
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break

    loop = input('\nDesideri continuare ad usare l\'applicazione? S/N ')
    if loop == "S" or loop == "s":
        print('''Sto tornando al Menù principale!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        continue    #passo al prossimo ciclo(giro) del while
    else:
        print('''Grazie e arrivederci!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break  #esco dal while

#Uscita while