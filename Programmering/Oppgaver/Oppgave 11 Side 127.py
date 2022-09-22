# Write a program that asks the user for the number of males and the number of females registered in the class
# The program should display the percentage of males and females in the class.

# Spør bruker om inndata
antall_gutter=int(input('Hvor mange gutter er det registrert i klassen din? '))
antall_jenter=int(input('Hvor mange jenter er det registrert i klassen din? '))

# Gjør om antall gutter/jenter til desimaltall
antall_elever=antall_gutter+antall_jenter

desimal_gutter=antall_gutter/antall_elever
desimal_jenter=antall_jenter/antall_elever

# Gjør om til prosent.

prosent_gutter=desimal_gutter*100
prosent_jenter=desimal_jenter*100

# Skriver ut prosentandel.
print('Det er',prosent_gutter,'% gutter i klassen og',prosent_jenter,'% jenter i klassen din')
      
