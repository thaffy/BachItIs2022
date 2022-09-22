def dobbel_verdi(dobbel_verdiTall):
    dobbel = 2 * dobbel_verdiTall
    print('Dobbel verdi av heltallet er',dobbel)

def main():
    tall = int(input('Oppgi tall: '))

    dobbel_verdi(tall)


main()

# Her får vi kjørefeil fordi tall ikke er global variabel,
# lokal variabel i funksjonen main
# og er da ukjent for funksjonen dobbel_verdi

# Dette løser vi ved parameteroverføring
