nimet = set()

while True:
    nimi = input('Syötä nimi tai lopeta painamalla enter: ')
    if nimi == "":
        break
    if nimi in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        nimet.add(nimi)
        print('Uusi nimi.')

print('Syötetyt nimet mielivaltaisessa järjestyksessä: ')
for nimi in nimet:
    print(nimi)