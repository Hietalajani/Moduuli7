airports = {"EFHK":"Helsinki", "EKCH":"Kööpenhamina",
            "ESSA":"Tukholma Arlanda", "ENGM":"Oslo",
            "LEMD":"Madrid", "LFPG":"Pariisi", "4WA1": "Kap Horn"}

while True:
    syöte = input('"Uusi" jos haluat syöttää uuden lentokentän, "Haku" jos haluat hakea lentokenttää, enter lopettaa: ')
    if syöte == "":
        print('Hyvää päivänjatkoa!')
        break
    elif syöte == "uusi".lower():
        ICAO = input('Syötä ICAO-koodi: ').upper()
        nimi = input('Syötä nimi: ').capitalize()
        airports[ICAO] = nimi
    elif syöte == "haku".lower():
        koodi = input('Syötä ICAO-koodi: ').upper()
        if koodi in airports:
            print(f'Lentokentän nimi: {airports[koodi]}.')
        else:
            print('Lentokenttää ei löydy.')
    else:
        print('Syöte ei vastaa mitään komentoa.')
