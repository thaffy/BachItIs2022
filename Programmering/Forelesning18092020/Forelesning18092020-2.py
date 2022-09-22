# WHILE løkke
# - betingelseskontrollert løkkestruktur
# - pretestet, dvs test før utførelse
# - løkkevariabelen må få verdi før og i løkka. Har løkkevariabelen verdi før løkka og i løkka?

# FOR løkke
# - tellekontrollert løkkestruktur
# - hvis vi vet hvor mange ganger programmet skal kjøres..


#Inndatatest i begynnelsen på programmet

#Variabel til bruk i inndatatest, bolsk variabel
nytt_tall=True

#Løkke som sikrer oss nytt tall
while nytt_tall==True:
    #Brukeren oppgir verdi på ruletten
    tall=int(input('Hva er tallet på ruletten? '))

    #Tester om gyldig verdi
    if tall>=0 and tall<=36:
        print('Gyldig verdi')
        nytt_tall=False
    else:
        print('Ugyldig verdi på ruletten. Skriv inn nytt tall.')

print('Da har vi fått et gyldig tall på ruletten og kan fortsette programmet med å avgjøre riktig farge')


