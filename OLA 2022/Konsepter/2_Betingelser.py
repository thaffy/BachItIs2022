### 1.0 - IF-statement ###

# Hvis noe er sant, gjør noe

testvariabel = 5 # <- Endrer vi denne fra 5 til 6 vil if-test nr 2 oppfylles, men ikke if-test nr 1

if testvariabel == 5:
    print('Tall: 5 - IF-test nr 1')
if testvariabel == 6:
    print('Tall: 6 - IF-test nr 2')

# Merk at vi bruker dobbel == i testene over
# dobbel == betyr i praksis at det vi tester på (testvariabel) er nøyaktig lik noe (5 eller 6)
# singel = er mest brukt i definering av en variabel
print()



if testvariabel != 5:
    print('Tall: ikke 5 - IF-test nr 3')
if testvariabel != 6:
    print('Tall: Ikke 6 - IF-test nr 4')

# != betyr at vi tester om noe er ulikt (er ikke)
# i eksempelet over betyr det at vi tester om testvariabel er ULIK 5 i test nr 3
# og i test nr 4 sjekker vi om testvariabel er ULIK 6
# resultatet er at test nr 3 ikke stemmer og ingenting skjer
# men resultatet i test nr 4 er sant og printer ut tekst.
print()



