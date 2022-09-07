vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kknumero = int(input('Anna kuukauden numero: '))

if kknumero == 12 or 1 <= kknumero <= 2:
    print(f'Kuukauden vuodenaika on {vuodenajat[3]}.')
elif 3 <= kknumero <= 5:
    print(f'Kuukauden vuodenaika on {vuodenajat[0]}.')
elif 6 <= kknumero <= 8:
    print(f'Kuukauden vuodenaika on {vuodenajat[1]}.')
elif 9 <= kknumero <= 11:
    print(f'Kuukauden vuodenaika on {vuodenajat[2]}.')
else:
    print('Kuukausia on 12 senkin hömelö.')
