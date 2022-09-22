def full_utskrift():
    print('--')
    print('Full utskrift')

    studenter = []
    antall_poster = 0
    studentfil = open('Studenter.txt','r',encoding='utf-8')

    studnr = studentfil.readline()
    

    while studnr != '':
        
        fornavn = studentfil.readline()
        etternavn = studentfil.readline()
        epost = studentfil.readline()
        fodt = studentfil.readline()
        kjonn = studentfil.readline()
        studium = studentfil.readline()
        
        studnr = studnr.rstrip('\n')
        fornavn = fornavn.rstrip('\n')
        etternavn = etternavn.rstrip('\n')
        epost = epost.rstrip('\n')
        fodt = fodt.rstrip('\n')
        kjonn = kjonn.rstrip('\n')
        studium = studium.rstrip('\n')

        studenter += [[studnr,fornavn,etternavn,epost,fodt,kjonn,studium ]]

        studnr = studentfil.readline()

    studentfil.close()

    antall_poster = len(studenter)

    print('Fornavn - Etternavn - Epost - Født - Kjønn - Studie')
    c = 0
    for r in range(antall_poster):
        print(studenter[r][c],studenter[r][c+1],studenter[r][c+2],studenter[r][c+3],studenter[r][c+4],studenter[r][c+5],studenter[r][c+6])
    
    
    
    

def kort_utskrift():
    print('--')
    print('Kort utskrift')

    studenter = []
    antall_poster = 0
    studentfil = open('Studenter.txt','r',encoding='utf-8')

    studnr = studentfil.readline()
    

    while studnr != '':
        
        fornavn = studentfil.readline()
        etternavn = studentfil.readline()
        epost = studentfil.readline()
        fodt = studentfil.readline()
        kjonn = studentfil.readline()
        studium = studentfil.readline()
        
        studnr = studnr.rstrip('\n')
        fornavn = fornavn.rstrip('\n')
        etternavn = etternavn.rstrip('\n')
        epost = epost.rstrip('\n')
        fodt = fodt.rstrip('\n')
        kjonn = kjonn.rstrip('\n')
        studium = studium.rstrip('\n')

        studenter += [[studnr,fornavn,etternavn,epost,fodt,kjonn,studium ]]

        studnr = studentfil.readline()

    studentfil.close()

    antall_poster = len(studenter)

    print('Fornavn - Etternavn - Epost')
    c = 0
    for r in range(antall_poster):
        print(studenter[r][c+1],studenter[r][c+2],' - Epost:',studenter[r][c+3])

def utskrift_kvinner():
    print('--')
    print('Utskrift kvinner')

    studenter = []
    antall_poster = 0
    studentfil = open('Studenter.txt','r',encoding='utf-8')

    studnr = studentfil.readline()
    

    while studnr != '':
        
        fornavn = studentfil.readline()
        etternavn = studentfil.readline()
        epost = studentfil.readline()
        fodt = studentfil.readline()
        kjonn = studentfil.readline()
        studium = studentfil.readline()
        
        studnr = studnr.rstrip('\n')
        fornavn = fornavn.rstrip('\n')
        etternavn = etternavn.rstrip('\n')
        epost = epost.rstrip('\n')
        fodt = fodt.rstrip('\n')
        kjonn = kjonn.rstrip('\n')
        studium = studium.rstrip('\n')

        studenter += [[studnr,fornavn,etternavn,epost,fodt,kjonn,studium ]]

        studnr = studentfil.readline()

    studentfil.close()

    antall_poster = len(studenter)

    c = 0
    print('Kvinner ved USN')
    print('Fornavn - Etternavn - Epost')
    for r in range(antall_poster):
        if studenter[r][c+5] == 'Kvinne':

            print(studenter[r][c+1],studenter[r][c+2],studenter[r][c+3])

def utskrift_it_og_is():
    print('--')
    print('Utskrift Bach IT og IS')

    studenter = []
    antall_poster = 0
    studentfil = open('Studenter.txt','r',encoding='utf-8')

    studnr = studentfil.readline()
    

    while studnr != '':
        
        fornavn = studentfil.readline()
        etternavn = studentfil.readline()
        epost = studentfil.readline()
        fodt = studentfil.readline()
        kjonn = studentfil.readline()
        studium = studentfil.readline()
        
        studnr = studnr.rstrip('\n')
        fornavn = fornavn.rstrip('\n')
        etternavn = etternavn.rstrip('\n')
        epost = epost.rstrip('\n')
        fodt = fodt.rstrip('\n')
        kjonn = kjonn.rstrip('\n')
        studium = studium.rstrip('\n')

        studenter += [[studnr,fornavn,etternavn,epost,fodt,kjonn,studium ]]

        studnr = studentfil.readline()

    studentfil.close()

    antall_poster = len(studenter)
    studentfil = open('Studenter.txt','r',encoding='utf-8')

    studnr = studentfil.readline()
    

    while studnr != '':
        
        fornavn = studentfil.readline()
        etternavn = studentfil.readline()
        epost = studentfil.readline()
        fodt = studentfil.readline()
        kjonn = studentfil.readline()
        studium = studentfil.readline()
        
        studnr = studnr.rstrip('\n')
        fornavn = fornavn.rstrip('\n')
        etternavn = etternavn.rstrip('\n')
        epost = epost.rstrip('\n')
        fodt = fodt.rstrip('\n')
        kjonn = kjonn.rstrip('\n')
        studium = studium.rstrip('\n')

        studenter += [[studnr,fornavn,etternavn,epost,fodt,kjonn,studium ]]

        studnr = studentfil.readline()

    studentfil.close()

    antall_poster = len(studenter)
    c = 0

    for r in range(antall_poster):
        if studenter[r][c+6] == 'Bach IT og IS':
            print(studenter[r][c],studenter[r][c+1],studenter[r][c+2],studenter[r][c+3],studenter[r][c+4],studenter[r][c+5])
            
def varesortering():
    print('--')
    print('Boblesortering av vare.txt')

def dictionary1():
    print('--')
    print('Opptelling med dictionary')

def dictionary2():
    print('--')
    print('Dictionary i dictionary')


def main():

    print('-- Studieadministrasjon')
    print('--')
    print('-- Velg program:')
    print('--')
    print('--')
    print('-- Delprogram 1 - Full utskrift')
    print('-- Delprogram 2 - Fornavn, etternavn og epostadresse')
    print('-- Delprogram 3 - Fornavn, etternavn, epostadresse for kvinner')
    print('-- Delprogram 4 - Studnr, fornavn, etternavn, kjønn for Bach IT og IS')
    print('--')
    print('-- Delprogram 5 - Boblesortering av elementene i Vare.txt')
    print('-- Delprogram 6 - Dictionary med opptelling')
    print('-- Delprogram 7 - Dictionary i dictionary med opptelling')

    svar = input('Hvilket program vil du kjøre? ')
    if svar == '1':
        full_utskrift()
    else:
        if svar == '2':
            kort_utskrift()
        else:
            if svar == '3':
                utskrift_kvinner()
            else:
                if svar =='4':
                    varesortering()
                else:
                    if svar =='5':
                        dictionary1()
                    else:
                        dictionary2()


main()
