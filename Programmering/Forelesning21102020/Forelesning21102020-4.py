# Program for å lese navn for navn og skrive ut de navnene som passer med søkekriteriet
# Generell fremgangsmåte, jfr fig 6-17 og program 6-9

# Åpner fila student.txt
studentfil=open('student.txt','r')

# Leser første linje i fila ved bruk av readline-metoden
student=studentfil.readline()

# I Python, readline returnerer en tom streng ('') når en har forsøkt å lese forbi "the end of file"/eof. Da tester vi på det.
print('Studenter med forbokstav "O": ')
while student!='':
    if student[0]=='O':
        print(student)
        
    # Leser ny linje fra fil
    student=studentfil.readline()

# Stenger fila
studentfil.close()


