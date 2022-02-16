###############################################
# Sortering av en vanlig liste med tall.
from tkinter import N


liste = [1,5,4,7,12,78,67,54,3,2,55,43,32,13,14,1,90,87]
print(liste)

# For sortering bruker vi to forløkker med variablene i og j
# tenk på i som ytreløkke-teller og j som indreløkke-teller
# i praksis betyr dette at for hver gang i gjør én gjennomgang så gjør j x antall gjennomganger, 
# basert på telleren til i samt listelengden


listelengde = len(liste)

for i in range(listelengde-1): # <- Ytre løkke
    for j in range(0,listelengde-i-1): # <- Indre Løkke
        if liste[j] > liste[j+1]: # < - Sjekker om elementene skal byttes
            liste[j],liste[j + 1] = liste[j + 1], liste[j] # <- Gjør bytte
print(liste)
print()


#        [0]  [1]  [2]  [3]   [4] ---->
liste = ['mann','dame','bil','tog','fly','fugl','vann','sjø','sko']
print(liste[4])

# #        [n]    [n+1]     [n+2]    [n+3] ] ---->
# liste = [mann,damejakke,bilmotor,togstasjon,fly,fugl,vann,sjø,sko]

# #           [0][0]     [0][1]      [1][0]      [1][1]
# liste = [[hoppeslott,togstasjon],[helikopter,ryggsekk]]

# #           [n][0]    [n][1]       [n+1][0]   [n+1][1]
# liste = [[hoppeslott,togstasjon],[helikopter,ryggsekk]]
# print(liste[n+1][1])






