# Program for å skrive 3 navn til en ny fil.

# Definerer og åpner fila student.txt
studentfil=open('student.txt','w')

# Skriver 3 navn til fila
# hver tekststreng slutter med \n, "the newline escape sequence", jfr s89 og s315-316
studentfil.write('Torvald\n')
studentfil.write('Kari\n')
studentfil.write('Jens\n')

# Stenger fila

studentfil.close()


