# Eksempel på hva en variabel er, blant annet.

### 0.0 - Aller først...

# er tegnet for kommentar. Alt som skrives etter # vil ikke kjøre/ødelegge for programmet.
# print() brukes for å skrive ut innhold i konsollen når du kjører programmet.
# print() brukes på følgende måte: print(innhold) eller print('Tekst') eller print('Tekst',tall/utregning,variabel)

print('Hei verden!')
print('Dette er en eksempeltekst. Hva er 2+2? Svar:',2+2)
print() # <- Tom print for å lage plass i konsollen









### 1.0 - Variabel ###

# I dette eksempelet skrives utregningene direkte i en print() for å vise resultatet i terminalen.
print(2+2)
print(2 + 5 * 10)
print((10*5-3) * (10+5-4))
print()                         

# Hvis vi nå har lyst å legge til alle sammen i ètt regnestykke så blir det litt tungvindt å skrive regnestykket for hver gang vi vil printe det.
# Eksempel:
print(2+2 + (2 + 5 * 10) + ((10*5-3) * (10+5-4))) # <- Det blir etterhvert vanskelig å holde styr på parantesene!
                                                  # <- Hvis vi har lyst å huske/kun gjøre denne utregningen èn gang, med mulighet for å legge til flere regnestykker i totalen
                                                  # <- så er det bedre å legge regnestykket inn i en variabel!
print()


regnestykke = 2 + 2 + (2 + 5 * 10) + ((10*5-3) * (10+5-4))
print(regnestykke)
print()

# Vi kan også dele opp regnestykket i flere ulike variabeler.
utregning1 = 2 + 2
utregning2 = 2 + 5 * 10
utregning3 = (10*5-3) * (10+5-4)
sum = utregning1 + utregning2 + utregning3
print(sum)
print()

# Vi kan også legge til tekst i en variabel:
tekst = 'Denne teksten er i en variabel.'
print(tekst)
print()









### 2.0 - Overskriving av variabler ###

# Hvis vi nå finner ut av at utregning1 var feil eller skal endre seg, kan vi overskrive den ved å bruke samme variabel navn
utregning1 = 2 + 100
sum = utregning1 + utregning2 + utregning3
print(sum)
print()

# Hvis vi vil legge til utregning2 inn i totalsummen i regnestykket så kan vi gjøre det ved bruk av utregning2-variabelen

sum = sum + utregning2 # <- Dette betyr at vi tar med oss den forrige verdien til sum, og legger til den nye
                       # <- Hvis vi hadde skrevet: sum = utregning2 så ville denne orginale verdien på sum blitt overskrevet
                       # <- Men, vi kan bruke kortformen += til å slippe unødvendig skriving. Da ser det sånn her ut:
                       # <- sum += utregning2 (Andre operatorer er: +=, -=, *=, /* )
print(sum)
print()

# Vi kan legge til mer tekst i variabelen vi lagde ovenfor:
tekst += ' Legger til mer tekst'
print(tekst)
print()







### 3.0 - Datatyper & Konvertering ###

# Kanskje vi legge til et tall?
# tekst += 1 <- Dette vil kræsje programmet.
# print(tekst)
#            <- Vi må skille mellom tall (int) og tekst (string).
#            <- Vi kan bruke metodene str() og int() for å konverte et tall til tekst eller en tekst til tall.

tekst += str(1)
print(tekst) # <- Her har tallet blitt lagt til på slutten av den orginale teksten.
print()

tall_tekst = '1' # < når vi har '' rundt noe i en variabel så teller det som tekst (eller string på engelsk)
tall_tekst_konvertering = int(tall_tekst) # <- Ettersom vi vet at det kun er tall i teksten, uten andre karakter så er konvertering til tall (eller integer på engelsk) ganske simpel
print(tall_tekst_konvertering)
print()

# Konvertering fra tall til tekst er som regel ganske problemfritt
sum_tekst = str(sum)
tekst += sum_tekst
print(tekst)
print()

# Det finnes flere datatyper enn string og int
# float er et desimaltall.
# vi kan konvertere en int (heltall) om til en float (desimaltall) via:
desimaltall = float(1)
print(desimaltall)
print()

# De andre datatypene kommer vi tilbake til senere.






