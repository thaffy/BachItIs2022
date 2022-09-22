# Program som simulerer test av disjunksjonen/ELLER mellom to logiske utsagn

print('Vi ønsker å vurdere A>3 ELLER B<6 for ulike verdier av A og B jfr forelesning 4 onsdag 16.09.2020')
print()

# I dette eksempelet bryter vi med at variabelnavn skal skrives med små bokstaver

# Verdien på A styres av en FOR-løkke fra og med verdien 2 til og med verdien 5
for A in range(2,6,1):
    # Verdien på B styres av en FOR-løkke fra og med verdien 4 til og med verdien 7
    for B in range(4,8,1):
        # Tester disjunksjonen
        if A>3 or B<6:
            print('Verdien på A er',A,'og verdien på B er',B,'og disjunksjonen er sann.')
        else:
            print('Verdien på A er',A,'og verdien på B er',B,'og disjunksjonen er usann.')
    print('Da er det slutt på løkka for å øke B med 1')
    print()
    print('Da øker verdien på A med 1')
print('Da er det slutt på løkka for å øke A med 1, og dermed slutt på programmet')
    
