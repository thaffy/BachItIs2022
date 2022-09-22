def dobbel_verdi():
    dobbel = 2 * tall
    print('Dobbel verdi av heltallet er',dobbel)

def main():
    tall = int(input('Oppgi tall: '))

    dobbel_verdi()


main()

# Her får vi kjørefeil fordi tall ikke er global variabel,
# lokal variabel i funksjonen main
# og er da ukjent for funksjonen dobbel_verdi
