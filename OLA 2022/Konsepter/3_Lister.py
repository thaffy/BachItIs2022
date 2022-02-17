### Lister ###

### 1.0 - Oppretting (definering) av en liste ###

# Oppretting av en tom liste
liste = []

# Oppretting av en liste med elementer
liste2 = ['Første','Andre','Tredje','Fjerde'] # <- Hvis elementene i listen er tekst (String) må vi ha '' rundt hvert element.
liste3 = [1,2,3,4,5,6,7,8,9,10] # <- Hvis elemtene i listen er tall eller variabler slipper vi å bruke ''





### 2.0 - Innskriving i lister ###
# Vi kan legge til element i en eksisterende liste med += eller ved å skrive liste = liste + [listeelement]
liste = liste + [1]
liste2 += ['Femte']
liste3 += [11]








### 3.0 - Utskrift av lister ###
# Vi kan skrive ut hele lister ved å skrive ut listevariabelen:
print(liste)
print(liste2)
print(liste3)
print()

# For å hente ut ètt enkelt element bruker vi følgende skrivemåte: liste[n] hvor n er plassen i lista elementet er på
# Hvis vi bruker listen under som eksempel. Legg merke til kommentaren direkte over listen

#           [0]       [1]     [2]     [3]
liste4 = ['Første','Andre','Tredje','Fjerde'] 

# Hvis vi nå har lyst å skrive ut ordet "Tredje", som er på listeplass 2 så gjør vi følgende:
print(liste4[2]) # <- Legg merke til at ordet "Tredje" er element nr 3 i lista, men vi begynner å teller fra 0.
                 # <- Derfor må vi bruke [2] i stedet for [3] hvis vi vil ha element nr 3 i lista!
print()







### 4.0 - 2-Dimensjonale Lister ###

# Det er kanskje mest naturlig visualisere en liste horisontalt, ettersom vi skriver elementene inn i lista horisontalt [1,2,3,4,5 --->], men egentlig er lister tabeller.
# En èndimensjonal liste er da en tabell med 1 kolonno og 1 rad.
# En todimensjonal liste blir da en tabell med 2 kolonnor og 2 rader

# Vi kan se skrive og tenke på en èndimensjonal liste sånn her:
liste5 = [
    'Første', # [0]
    'Andre',  # [1]
    'Tredje', # [2]
    'Fjerde'  # [3]
]             # Merk at vi må ha komma mellom hvert element!

print('Liste nr 5:',liste5)
print()

# En todimensjonal liste kan vi skrive slik:
liste6 = [['Første',1,2,3,4],['Andre',5,6,7,8],['Tredje',9,10,11,12]]

# Eller slik:
liste7 = [
    ['Første',1,2,3,4],    # [0][0-4]
    ['Andre',5,6,7,8],     # [1][0-4]
    ['Tredje',9,10,11,12], # [2][0-4]
]                          # Merk at vi må ha komma mellom hvert element og sub-element!

# Begge måtene å skrive det i koden gir samme resultat:
print('Liste6:',liste6)
print('Liste7:',liste6)
print()


# Tenk at vi skal hente ut ordet 'Første' og tallet '4' i samme print. Vi vil ikke ha med noe annet.
# For å gjøre det må vi refere til kun de elementene vi vil ha

print(liste7[0][0],liste7[0][4])
print()

# For å demonstrere hvordan vi vet at printen er over korrekt kan vi se over tabellen:
# Legg merke til kommentarene

liste7 = [
    # Kolonner -->
    #  [0]  [1][2][3][4]
    ['Første',1,2,3,4],    # [0] Rad
    ['Andre',5,6,7,8],     # [1] Rad
    ['Tredje',9,10,11,12], # [2] Rad
]   

# liste7[0][0] blir da ordet 'Første', fordi det ordet befinner seg i første rad og første kolonne.
# liste7[0][1] blir da tallet 1, fordi det tallet befinner seg i første rad, andre kolonne
# liste7[1][0] blir da ordet 'Andre', fordi det ordet befinner seg i andre rad, første kolonne... osv

# Det kan være litt forvirrende at vi referer til 0 som første rad/kolonne, men det er bare slik det er! 
# Vi begynner som regel å telle fra 0 i mange sammenhenger, med mindre vi spesifiser noe annet