def main():
    print('Program for innlesing av informasjon fra tekstfil inn i to-dimensjonal liste.')
    print()

    kundeliste = []

    kundefil = open('Kunde.txt','r',encoding='utf-8')

    mobilnr = kundefil.readline()

    while mobilnr != '':
        mobilnr = mobilnr.rstrip('\n')

        fornavn = kundefil.readline().rstrip('\n')
        etternavn = kundefil.readline().rstrip('\n')
        epost = kundefil.readline().rstrip('\n')

        kundeliste += [[mobilnr,fornavn,etternavn,epost]]

        mobilnr = kundefil.readline()

    kundefil.close()

    listelengde = len(kundeliste)


    print('Mobilnr - Fornavn - Etternavn')
    for row in range(listelengde):
        print(kundeliste[row][0],kundeliste[row][1],kundeliste[row][2])


main()
