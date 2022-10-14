inntekst = True
liste = []
while inntekst == True:
    navn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    studie = input("Skriv inn studie: ")
    slutt = input("Stopp?")
    liste += [navn,etternavn,studie]
    
    if slutt == "ja":
        inntekst = False

        

listeIT = []
lengde = len(liste)
i = 0

for i in range(lengde):
    if liste[i] == 'IT':
        listeIT += liste[i-2],liste[i-1],liste[i]

print(liste)
print(listeIT)