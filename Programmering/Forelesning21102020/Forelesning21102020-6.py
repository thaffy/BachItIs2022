# Program for innføring i funksjoner/prosedyrer/delprogrammer
# Koden for programmet i en egen funksjon/prosedyre --> main()

def drommebolig():
    drommebolig_restart=True
    while drommebolig_restart==True:
        # Her kommer kode for kalkulator 1
        print()
        print('Du har valgt kalkulator 1, Drømmebolig.')
        
        

def lanebevis():
    # Her kommer kode for kalkulator 2
    print()
    print('Du har valgt kalkulator 2, Lånebevis.')


def main():
    # Her kommer koden for programmet - Valg av kalkulator og programrestart
    print('Her kan du kjøre 2 ulike kalkulatorer - Drømmebolig eller Lånebevis')
    fortsette=True

    while fortsette==True:
        valgt_kalkulator=int(input('Hvilken kalkulator vil du bruke? 1 eller 2: '))
        if valgt_kalkulator==1:
            drommebolig()
        else:
            lanebevis()
            
        svar=input('Ønsker du å bruke en av kalkulatorene på nytt? ')
        if svar=='nei' or svar=='Nei' or svar=='NEI':
            fortsette=False
            print()
            print('Program avsluttet.')

# Her kjøres main()
main()
