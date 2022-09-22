from tkinter import *
from datetime import datetime
import mysql.connector
oblig2021database = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef ', passwd='oblig2021', db='oblig2021')


def vinduRegistrerStudent():
    # F E R D I G
    vinduRegistrerStudent = Toplevel()
    vinduRegistrerStudent.title('Registrer Student')

    def genererStudentnr():
        student_markor = oblig2021database.cursor()
        student_markor.execute('SELECT MAX(Studentnr) AS Storste_studnr FROM Student')
        studnr = []
        studnr += student_markor
        storste_studentnr = int(studnr[0][0])
        nytt_studentnr = storste_studentnr + 1
        input_studentnr.set(nytt_studentnr)

        student_markor.close()
        

    def registrerStudent():
        # Det logiske laget i registrerStudent
        student_markor = oblig2021database.cursor()

        studentnr = input_studentnr.get()
        fornavn = input_fornavn.get()
        etternavn = input_etternavn.get()
        epost = input_epost.get()
        telefon = int(input_telefonnr.get())

        settinn_student = ('INSERT INTO Student'
                           '(Studentnr,Fornavn,Etternavn,Epost,Telefon)'
                           'VALUES(%s,%s,%s,%s,%s)'
                           )
        nystudent = (studentnr,fornavn,etternavn,epost,telefon)
        student_markor.execute(settinn_student,nystudent)
        oblig2021database.commit()
        student_markor.close()

        input_studentnr.set('')
        input_fornavn.set('')
        input_etternavn.set('')
        input_epost.set('')
        input_telefonnr.set('')
        output_lagret.set(fornavn + ' har blitt lagret!')
        lbl_lagret['fg']='green'
        

    ## GUI ##
    # Labels/ledetekst for informasjonen bruker skal oppgi
    lbl_RegistrerStudent = Label(vinduRegistrerStudent,text='Registrer Student')
    lbl_RegistrerStudent.grid(row=0,column=0,padx=10,pady=5,sticky=E)

    lbl_fornavn = Label(vinduRegistrerStudent,text='Fornavn')
    lbl_fornavn.grid(row = 2, column = 0, padx= 10, pady = 5, sticky = E)

    lbl_etternavn = Label(vinduRegistrerStudent,text='Etternavn')
    lbl_etternavn.grid(row = 3, column = 0, padx= 10, pady = 5, sticky = E)

    lbl_epost = Label(vinduRegistrerStudent,text='Epost')
    lbl_epost.grid(row = 4, column = 0, padx= 10, pady = 5, sticky = E)

    lbl_telefon = Label(vinduRegistrerStudent,text='Telefonnr')
    lbl_telefon.grid(row = 5, column = 0, padx= 10, pady = 5, sticky = E)

    # Entry-felt for informasjon
    input_studentnr = StringVar()
    entry_studentnr = Entry(vinduRegistrerStudent, width = 6, textvariable = input_studentnr, state='readonly')
    entry_studentnr.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)
    
    
    input_fornavn = StringVar()
    entry_fornavn = Entry(vinduRegistrerStudent,width=10,textvariable=input_fornavn)
    entry_fornavn.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    input_etternavn = StringVar()
    entry_etternavn = Entry(vinduRegistrerStudent,width=10,textvariable=input_etternavn)
    entry_etternavn.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    input_epost = StringVar()
    entry_epost = Entry(vinduRegistrerStudent,width=20,textvariable=input_epost)
    entry_epost.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    input_telefonnr = StringVar()
    entry_telefonnr = Entry(vinduRegistrerStudent,width=9,textvariable=input_telefonnr)
    entry_telefonnr.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = W)

    output_lagret = StringVar()
    lbl_lagret = Label(vinduRegistrerStudent, width = 20, textvariable = output_lagret)
    lbl_lagret.grid(row = 6,column = 0,padx = 10, pady = 5,sticky = E)

    # Knapper
    btn_studentnr = Button(vinduRegistrerStudent,text='Generer Studentnr',command = genererStudentnr)
    btn_studentnr.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    btn_lagre = Button(vinduRegistrerStudent,width = 7,text='Lagre', command = registrerStudent)
    btn_lagre.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduRegistrerStudent,text = 'Tilbake til hovedvindu',command = vinduRegistrerStudent.destroy)
    btn_tilbake.grid(row = 7, column = 2, padx = 10, pady = 5, sticky = E)


def vinduOppdaterStudent():
    # F E R D I G, men kan omskrives med mer spesifikk sql setning
    vinduOppdaterStudent = Toplevel()
    vinduOppdaterStudent.title('Endre Student')

    def sjekkStudentnr():
        student_markor = oblig2021database.cursor()
        student_markor.execute('SELECT * FROM Student')

        studentnrliste = []
        studentnrliste += student_markor

        listelengde = len(studentnrliste)
        studnr = input_studnr.get()
        funnet = False
        for row in range(listelengde):
            if studnr == studentnrliste[row][0]:
                funnet = True
                input_fornavn.set(studentnrliste[row][1])
                input_etternavn.set(studentnrliste[row][2])
                input_epost.set(studentnrliste[row][3])
                input_telefonnr.set(studentnrliste[row][4])
        student_markor.close()

    def oppdaterStudent():

        studnr = input_studnr.get()
        fornavn = input_fornavn.get()
        etternavn = input_etternavn.get()
        epost = input_epost.get()
        telefon = int(input_telefonnr.get())

        student_markor = oblig2021database.cursor()
        student_markor.execute('SELECT * FROM Student')

        studentnrliste = []
        studentnrliste += student_markor

        listelengde = len(studentnrliste)

        oppdater_student = ('UPDATE Student SET Fornavn = %s, Etternavn = %s, Epost = %s, Telefon = %s WHERE Studentnr = %s')
        student_info = (fornavn,etternavn,epost,telefon,studnr)
        student_markor.execute(oppdater_student,student_info)
        oblig2021database.commit()
            
        student_markor.close()

    ## GUI ##
    # Labels/ledetekst for informasjonen bruker skal oppgi
    lbl_OppdaterStudent = Label(vinduOppdaterStudent,text='Endre Student')
    lbl_OppdaterStudent.grid(row=0,column=0,padx=10,pady=5,sticky=E)

    lbl_fornavn = Label(vinduOppdaterStudent,text='Fornavn')
    lbl_fornavn.grid(row = 2, column = 0, padx= 10, pady = 5, sticky = E)

    lbl_etternavn = Label(vinduOppdaterStudent,text='Etternavn')
    lbl_etternavn.grid(row = 3, column = 0, padx= 10, pady = 5, sticky = E)

    lbl_epost = Label(vinduOppdaterStudent,text='Epost')
    lbl_epost.grid(row = 4, column = 0, padx= 10, pady = 5, sticky = E)

    lbl_telefon = Label(vinduOppdaterStudent,text='Telefonnr')
    lbl_telefon.grid(row = 5, column = 0, padx= 10, pady = 5, sticky = E)

    # Entry-felt for informasjon
    input_studnr = StringVar()
    entry_studnr = Entry(vinduOppdaterStudent,width=6,textvariable=input_studnr)
    entry_studnr.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)
    
    input_fornavn = StringVar()
    entry_fornavn = Entry(vinduOppdaterStudent,width=10,textvariable=input_fornavn)
    entry_fornavn.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    input_etternavn = StringVar()
    entry_etternavn = Entry(vinduOppdaterStudent,width=10,textvariable=input_etternavn)
    entry_etternavn.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    input_epost = StringVar()
    entry_epost = Entry(vinduOppdaterStudent,width=20,textvariable=input_epost)
    entry_epost.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    input_telefonnr = StringVar()
    entry_telefonnr = Entry(vinduOppdaterStudent,width=9,textvariable=input_telefonnr)
    entry_telefonnr.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = W)

    # Knapper
    btn_sjekkStudentnr = Button(vinduOppdaterStudent,text = 'Søk etter studentnr', command = sjekkStudentnr)
    btn_sjekkStudentnr.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    btn_lagre = Button(vinduOppdaterStudent, width = 7, text='Lagre', command = oppdaterStudent)
    btn_lagre.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduOppdaterStudent,text = 'Tilbake til hovedvindu',command = vinduOppdaterStudent.destroy)
    btn_tilbake.grid(row = 7, column = 2, padx = 10, pady = 5, sticky = E)

def vinduSlettStudent():
    vinduSlettStudent = Toplevel()
    vinduSlettStudent.title('Slett Student')
    # F E R D I G

    def sokStudnr():
        student_markor = oblig2021database.cursor()
        studentnr = str(input_studnr.get())

        
        sqlsok = ('SELECT * FROM Student WHERE Studentnr=%s')
        sql_studentnr = (studentnr,)
        student_markor.execute(sqlsok,sql_studentnr)

        student_liste = []
        student_liste += student_markor
        student_markor.close()

        if student_liste:
            studentFinnes.set('Verifiser studentinformasjonen.')
            input_fornavn.set(student_liste[0][1])
            input_etternavn.set(student_liste[0][2])
            input_epost.set(student_liste[0][3])
            input_telefon.set(student_liste[0][4])
        else:
            studentFinnes.set('Studenten eksisterer ikke!')

    def slettStudent():
        student_markor = oblig2021database.cursor()
        
        studentnr = input_studnr.get()
        fornavn = input_fornavn.get()
        etternavn = input_etternavn.get()
        epost = input_epost.get()
        telefon = input_telefon.get()

        sql_slett = ('DELETE FROM Student WHERE Studentnr = %s')
        data_slettstudent = (studentnr,)
        student_markor.execute(sql_slett,data_slettstudent)
        oblig2021database.commit()
        student_markor.close()

        # Entry-feltene blir satt til å være tomme når informasjonen er sendt til databasen.
        studentFinnes.set('')
        input_studnr.set('')
        input_fornavn.set('')
        input_etternavn.set('')
        input_epost.set('')
        input_telefon.set('')
        
   
    ## GUI ##
    # Labels
    lbl_slettStudent = Label(vinduSlettStudent,text='Slett student')
    lbl_slettStudent.grid(row = 0,column = 0,padx = 10,pady = 5,sticky = W)

    studentFinnes = StringVar()
    lbl_oppgiStudnr = Label(vinduSlettStudent, textvariable = studentFinnes)
    lbl_oppgiStudnr.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    lbl_fornavn = Label(vinduSlettStudent,text = 'Fornavn')
    lbl_fornavn.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_etternavn = Label(vinduSlettStudent, text = 'Etternavn')
    lbl_etternavn.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_epost = Label(vinduSlettStudent, text = 'Etternavn')
    lbl_epost.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_telefon = Label(vinduSlettStudent, text = 'Telefonnr')
    lbl_telefon.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = E)

    # Entry felt
    input_studnr = StringVar()
    entry_studnr = Entry(vinduSlettStudent, width = 6,textvariable = input_studnr)
    entry_studnr.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    input_fornavn = StringVar()
    entry_fornavn = Entry(vinduSlettStudent, width = 10, state = 'readonly', textvariable = input_fornavn)
    entry_fornavn.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    input_etternavn = StringVar()
    entry_etternavn = Entry(vinduSlettStudent, width = 10, state = 'readonly', textvariable = input_etternavn)
    entry_etternavn.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    input_epost = StringVar()
    entry_epost = Entry(vinduSlettStudent, width = 20, state = 'readonly', textvariable = input_epost)
    entry_epost.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = W)

    input_telefon = StringVar()
    entry_telefon = Entry(vinduSlettStudent, width = 9, state ='readonly', textvariable = input_telefon)
    entry_telefon.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = W)

    # Knapper
    btn_sokStudnr = Button(vinduSlettStudent,text='Søk etter studentnr',command = sokStudnr)
    btn_sokStudnr.grid(row=1,column = 0,padx = 10, pady = 5, sticky = E)

    btn_slettStudent = Button(vinduSlettStudent, text = 'Slett Student', command = slettStudent)
    btn_slettStudent.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduSlettStudent,text = 'Tilbake til hovedvindu',command = vinduSlettStudent.destroy)
    btn_tilbake.grid(row = 8, column = 2, padx = 10, pady = 5, sticky = E)
    

def vinduOpprettEksamen():
    # F E R D I G
    vinduOpprettEksamen = Toplevel()
    vinduOpprettEksamen.title('Opprett Eksamen')

    def opprettEksamen():
        opprett_markor = oblig2021database.cursor()
        opprett_markor.execute('SELECT * FROM Eksamen')

        eksisterende_eksamener = []
        eksisterende_eksamener += opprett_markor

        emnekode = input_emnekode.get()
        dato = input_dato.get()
        romnr = input_romnr.get()

        formatert_dato = datetime.strptime(dato, '%Y%m%d').strftime('%Y-%m-%d')
        listelengde = len(eksisterende_eksamener)
        rom_opptatt = False

        # Test på om rommet er opptatt fra før.
        for row in range(listelengde):
            if (str(eksisterende_eksamener[row][1]) == str(formatert_dato)) and (eksisterende_eksamener[row][2] == romnr):
                rom_opptatt = True
        if rom_opptatt == True:
                # Gjør om til dynamisk read-only entry senere
                lbl_opptatt = Label(vinduOpprettEksamen,text = 'Rommet er opptatt!')
                lbl_opptatt.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = E)
        else:
            settinn_eksamen = ('INSERT INTO Eksamen'
                               '(Emnekode,Dato,Romnr)'
                               'VALUES(%s,%s,%s)'
                               )
            data_nyeksamen = (emnekode,dato,romnr)
            opprett_markor.execute(settinn_eksamen,data_nyeksamen)
            oblig2021database.commit()
            
        opprett_markor.close()

    ## GUI ##
    # Labels
    lbl_eksamen = Label(vinduOpprettEksamen,text='Opprett Eksamen')
    lbl_eksamen.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

    lbl_emnekode = Label(vinduOpprettEksamen,text='Emnekode')
    lbl_emnekode.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_dato = Label(vinduOpprettEksamen,text='Dato')
    lbl_dato.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_romnr = Label(vinduOpprettEksamen,text='Romnr')
    lbl_romnr.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = E)

    # Entryfelt
    input_emnekode = StringVar()
    entry_emnekode = Entry(vinduOpprettEksamen,width = 7,textvariable = input_emnekode)
    entry_emnekode.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    input_dato = StringVar()
    entry_dato = Entry(vinduOpprettEksamen,width = 8, textvariable = input_dato)
    entry_dato.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    input_romnr = StringVar()
    entry_romnr = Entry(vinduOpprettEksamen,width = 4, textvariable = input_romnr)
    entry_romnr.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    # Knapper
    btn_lagre = Button(vinduOpprettEksamen,width = 7,text = 'Lagre',command = opprettEksamen)
    btn_lagre.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduOpprettEksamen,text = 'Tilbake til hovedvindu',command = vinduOpprettEksamen.destroy)
    btn_tilbake.grid(row = 5, column = 2, padx = 10, pady = 5, sticky = E)
    
    
    

def vinduEndreEksamen():
    # F E R D I G
    # Vindu for å endre eller oppdatere en oppsatt eksamen.
    vinduEndreEksamen = Toplevel()
    vinduEndreEksamen.title('Endre Eksamen')

    def sjekkEksamen():
        # Funksjonen for å søke etter eksamenen i databasen basert på brukers input.

        def endreEksamen():
            # Funksjonen for å endre/oppdatere eksamenen når den er funnet.
            eksamen_markor = oblig2021database.cursor()

            # Informasjonen bruker har oppgitt blir hentet inn. Dette er den "nye" informasjonen, hvis noen av Entry-feltene har blitt endret på.
            emnekode = input_emnekode.get()
            dato = int(input_dato.get())
            rom = input_rom.get()
            # Informasjonen som opprinnelig lå i databasen blir hentet ut fra eksamen_liste og satt i sine egne variabler. 
            opprinneligEmnekode = eksamen_liste[0][0]
            opprinneligDato = eksamen_liste[0][1]
            opprinneligRom = eksamen_liste[0][2]

            # SQL spørring for å se om rommet er opptatt på oppgitt dato
            eksamen_sjekk = ('SELECT * FROM Eksamen WHERE Dato = %s AND Romnr = %s')
            eksamen_sjekkData = (dato,rom)
            eksamen_markor.execute(eksamen_sjekk,eksamen_sjekkData)

            sjekkliste = []
            sjekkliste += eksamen_markor

            if sjekkliste:
                endreInfo.set('Rommet er opptatt denne datoen.')
            else:
                eksamen_sql = ('UPDATE Eksamen SET Emnekode = %s, Dato = %s, Romnr = %s WHERE Emnekode = %s AND Dato = %s AND Romnr = %s')
                eksamen_data = (emnekode,dato,rom,opprinneligEmnekode,opprinneligDato,opprinneligRom)

                eksamen_markor.execute(eksamen_sql,eksamen_data)
                oblig2021database.commit()

                # Oppdaterer GUI-elementene
                endreInfo.set('Eksamenen har blitt oppdatert!')
                input_emnekode.set('')
                input_dato.set('')
                input_rom.set('')
                

            eksamen_markor.close()


        eksamen_markor = oblig2021database.cursor()

        emnekode = input_emnekode.get()
        dato = input_dato.get()

        eksamen_sql = ('SELECT * FROM Eksamen WHERE Emnekode = %s AND Dato = %s')
        eksamen_sokdata = (emnekode,dato)
        eksamen_markor.execute(eksamen_sql,eksamen_sokdata)
        

        eksamen_liste = []
        eksamen_liste += eksamen_markor


        if eksamen_liste:
            endreInfo.set('Oppdater informasjon og trykk Lagre.')
            input_rom.set(eksamen_liste[0][2])
            
            btn_endreEksamen = Button(vinduEndreEksamen,text = 'Lagre', command = endreEksamen)
            btn_endreEksamen.grid(row = 5, column = 2, padx = 10, pady = 5, sticky = W)
        else:
            endreInfo.set('Eksamenen eksisterer ikke.')
            
        eksamen_markor.close()

    ## GUI ##  
    # Labels
    lbl_endreEksamen = Label(vinduEndreEksamen, text = 'Endre en eksamen')
    lbl_endreEksamen.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

    lbl_emnekode = Label(vinduEndreEksamen, text = 'Emnekode')
    lbl_emnekode.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_dato = Label(vinduEndreEksamen, text = 'Dato')
    lbl_dato.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_rom = Label(vinduEndreEksamen, text = 'Romnr')
    lbl_rom.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = E)

    endreInfo = StringVar()
    lbl_endreinfo = Label(vinduEndreEksamen, textvariable = endreInfo)
    lbl_endreinfo.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = W)

    # Entryfelt
    input_emnekode = StringVar()
    entry_emnekode = Entry(vinduEndreEksamen,width = 7, textvariable = input_emnekode)
    entry_emnekode.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    input_dato = StringVar()
    entry_dato = Entry(vinduEndreEksamen, width = 8, textvariable = input_dato)
    entry_dato.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    input_rom = StringVar()
    entry_rom = Entry(vinduEndreEksamen, width = 4, textvariable = input_rom)
    entry_rom.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    # Knapper
    btn_sjekkEksamen = Button(vinduEndreEksamen,text = 'Søk etter emnekode og dato', command = sjekkEksamen)
    btn_sjekkEksamen.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduEndreEksamen,text = 'Tilbake til hovedvindu',command = vinduEndreEksamen.destroy)
    btn_tilbake.grid(row = 6, column = 2, padx = 10, pady = 5, sticky = E)


    

def vinduSlettEksamen():
    # F E R D I G
    vinduSlettEksamen = Toplevel()
    vinduSlettEksamen.title('Slett Eksamen')

    def slettEksamen():
        eksamen_markor = oblig2021database.cursor()
        eksamen_sql = ('DELETE FROM Eksamen WHERE Emnekode = %s AND Dato = %s AND Romnr = %s')

        emnekode = input_emnekode.get()
        dato = input_dato.get()
        romnr = input_rom.get()

        eksamen_data = (emnekode,dato,romnr)

        eksamen_markor.execute(eksamen_sql,eksamen_data)
        oblig2021database.commit()

        eksamen_markor.close()

        input_emnekode.set('')
        input_dato.set('')
        input_rom.set('')
        

    lbl_slettEksamen = Label(vinduSlettEksamen,text = 'Slett eksamen')
    lbl_slettEksamen.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

    lbl_emnekode = Label(vinduSlettEksamen,text = 'Emnekode')
    lbl_emnekode.grid(row = 1, column = 0, padx = 10, pady = 5, sticky =E)

    lbl_dato = Label(vinduSlettEksamen, text = 'Dato')
    lbl_dato.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_rom = Label(vinduSlettEksamen, text = 'Rom')
    lbl_rom.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = E)

    input_emnekode = StringVar()
    entry_emnekode = Entry(vinduSlettEksamen, width = 7, textvariable = input_emnekode)
    entry_emnekode.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    input_dato = StringVar()
    entry_dato = Entry(vinduSlettEksamen, width = 8, textvariable = input_dato)
    entry_dato.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    input_rom = StringVar()
    entry_rom = Entry(vinduSlettEksamen, width = 4, textvariable = input_rom)
    entry_rom.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    #btn_sok = Button(vinduSlettEksamen, text = 'Søk', command = sokEksamen)
    #btn_sok.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    btn_slettEksamen = Button(vinduSlettEksamen, text = 'Slett', command = slettEksamen)
    btn_slettEksamen.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduSlettEksamen,text = 'Tilbake til hovedvindu',command = vinduSlettEksamen.destroy)
    btn_tilbake.grid(row = 5, column = 2, padx = 10, pady = 5, sticky = E)
    


def vinduRegistrerResultat():
    # F E R D I G
    # Funksjonen for det meste av GUI-komponenter
    def sokEksamen():
        eksamen_markor = oblig2021database.cursor()



        
        # Funksjon for å hente valgt studentnr i listeboksen, samt vise lagre knapp.
        def valgtStudent(event):
            valgt = lst_studnr.get(lst_studnr.curselection())


            # Funksjon for å lagre resultat i mysql
            def lagreKarakter():

                karakter_markor = oblig2021database.cursor()
                studentnr = valgt
                karakter = input_karakter.get()

                lagreKarakter_sql = ('UPDATE Eksamensresultat SET Karakter = %s WHERE Studentnr = %s')
                karakter_nydata = (karakter,studentnr)

                karakter_markor.execute(lagreKarakter_sql,karakter_nydata)
                oblig2021database.commit()
                karakter_markor.close()

                input_karakter.set('')

                blittLagret = StringVar()
                blittLagret.set(studentnr +"'s karakter har blitt lagret!")
                lbl_blittLagret = Label(vinduRegistrerResultat, textvariable = blittLagret)
                lbl_blittLagret.grid(row = 3, column = 4, padx = 10, pady = 5, sticky = E)

            # Gui for lagring av karakter etter studnr er valgt
            btn_lagre = Button(vinduRegistrerResultat, text = 'Lagre',command = lagreKarakter)
            btn_lagre.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = E)

            
        eksamen_sql = ('SELECT * \
                        FROM Eksamensresultat \
                        WHERE Karakter IS NULL \
                            AND Emnekode = %s \
                            AND Dato = %s \
                        ORDER BY Studentnr')

        emnekode = input_emnekode.get()
        dato = input_dato.get()

        eksamen_data = (emnekode,dato)
        eksamen_markor.execute(eksamen_sql,eksamen_data)

        eksamen_liste = []
        eksamen_liste += eksamen_markor

        eksamen_markor.close()

        listelengde = len(eksamen_liste)

        # Lager en liste med kun studentnummer
        studnrliste = []
        for row in range(listelengde):
            studnrliste += [eksamen_liste[row][0]]

        y_scroll = Scrollbar(vinduRegistrerResultat, orient = VERTICAL)
        y_scroll.grid(row = 1, column = 3, rowspan = 10, padx = (0,100), pady = 5, sticky = NS)

        innhold_studnrliste = StringVar()
        lst_studnr = Listbox(vinduRegistrerResultat, width = 8, height = 10, listvariable = innhold_studnrliste, yscrollcommand = y_scroll.set)
        lst_studnr.grid(row = 1, column = 2, rowspan = 10, padx = (100,0), pady = 5, sticky = E)
        innhold_studnrliste.set(tuple(studnrliste))
        y_scroll["command"] = lst_studnr.yview

        lbl_karakter = Label(vinduRegistrerResultat,text = 'Karakter ')
        lbl_karakter.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = E)

        input_karakter = StringVar()
        entry_karakter = Entry(vinduRegistrerResultat,width = 1,textvariable = input_karakter)
        entry_karakter.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = E)
        lst_studnr.bind("<<ListboxSelect>>",valgtStudent)


        eksamen_markor.close()
        
    vinduRegistrerResultat = Toplevel()
    vinduRegistrerResultat.title('Registrer Eksamensresultat')

    lbl_registrerResultat = Label(vinduRegistrerResultat,text = 'Registrer eksamensresultat')
    lbl_registrerResultat.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

    lbl_emnekode = Label(vinduRegistrerResultat,text = 'Emnekode')
    lbl_emnekode.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_dato = Label(vinduRegistrerResultat,text = 'Dato')
    lbl_dato.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = E)

    input_emnekode = StringVar()
    entry_emnekode = Entry(vinduRegistrerResultat, width = 7, textvariable = input_emnekode)
    entry_emnekode.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    input_dato = StringVar()
    entry_dato = Entry(vinduRegistrerResultat, width = 8, textvariable = input_dato)
    entry_dato.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    btn_sokEksamen = Button(vinduRegistrerResultat, text = 'Søk eksamen',command = sokEksamen)
    btn_sokEksamen.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = E)

    btn_tilbake = Button(vinduRegistrerResultat,text = 'Tilbake til hovedvindu',command = vinduRegistrerResultat.destroy)
    btn_tilbake.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = E)

def vinduEndreResultat():
    # F E R D I G
    vinduEndreResultat = Toplevel()
    vinduEndreResultat.title('Endre Eksamensresultat')

    def sokResultat():
        studnr = input_studnr.get()
        emnekode = input_emnekode.get()
        dato = input_dato.get()

        resultat_markor = oblig2021database.cursor()

        resultat_sql = ('SELECT * FROM Eksamensresultat \
                        WHERE Studentnr = %s AND Emnekode = %s AND Dato = %s')
        resultat_data = (studnr,emnekode,dato)
        resultat_markor.execute(resultat_sql,resultat_data)

        resultat_liste = []
        resultat_liste += resultat_markor

        if resultat_liste:
            opprinnelig_karakter = resultat_liste[0][3]
            input_karakter.set(opprinnelig_karakter)
            
        resultat_markor.close()

    def endreResultat():
        studnr = input_studnr.get()
        emnekode = input_emnekode.get()
        dato = input_dato.get()
        karakter = input_karakter.get()

        resultat_markor = oblig2021database.cursor()

        update_sql = ('UPDATE Eksamensresultat SET Karakter = %s WHERE Studentnr = %s AND Emnekode = %s AND Dato = %s')
        update_data = (karakter,studnr,emnekode,dato)

        resultat_markor.execute(update_sql,update_data)
        oblig2021database.commit()

        resultat_markor.close()

        input_studnr.set('')
        input_emnekode.set('')
        input_dato.set('')
        input_karakter.set('')
        
        
    lbl_endreResultat = Label(vinduEndreResultat, text = 'Endre eksamensresultat')
    lbl_endreResultat.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

    lbl_studnr = Label(vinduEndreResultat,text = 'Studentnr')
    lbl_studnr.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_emnekode = Label(vinduEndreResultat,text = 'Emnekode')
    lbl_emnekode.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_dato = Label(vinduEndreResultat,text = 'Dato')
    lbl_dato.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_karakter = Label(vinduEndreResultat, text = 'Karakter')
    lbl_karakter.grid(row = 5,column = 0, padx = 10, pady = 5, sticky = E)

    input_studnr = StringVar()
    entry_studnr = Entry(vinduEndreResultat, width = 6, textvariable = input_studnr)
    entry_studnr.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    input_emnekode = StringVar()
    entry_emnekode = Entry(vinduEndreResultat, width = 7, textvariable = input_emnekode)
    entry_emnekode.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    input_dato = StringVar()
    entry_dato = Entry(vinduEndreResultat,width = 8, textvariable = input_dato)
    entry_dato.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    input_karakter = StringVar()
    entry_karakter = Entry(vinduEndreResultat, width = 1, textvariable = input_karakter)
    entry_karakter.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = W)
    
    btn_sok = Button(vinduEndreResultat, text = 'Søk',command = sokResultat)
    btn_sok.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    btn_lagre = Button(vinduEndreResultat,width = 7,text = 'Lagre',command = endreResultat)
    btn_lagre.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduEndreResultat,text = 'Tilbake til hovedvindu',command = vinduEndreResultat.destroy)
    btn_tilbake.grid(row = 7, column = 2, padx = 10, pady = 5, sticky = E)
    
def vinduSlettResultat():
    # F E R D I G
    vinduSlettResultat = Toplevel()
    vinduSlettResultat.title('Slett Eksamensresultat')

    def sokKarakter():
        karakter_markor = oblig2021database.cursor()

        studentnr = input_studnr.get()
        emne = input_emne.get()
        dato = input_dato.get()

        eksamen_sql = ('SELECT * FROM Eksamensresultat WHERE Studentnr = %s AND Emnekode = %s AND Dato = %s')
        input_data = (studentnr, emne, dato)

        karakter_markor.execute(eksamen_sql,input_data)
        karakter_liste = []
        karakter_liste += karakter_markor

        if karakter_liste:
            karakter = karakter_liste[0][3]
            input_karakter.set(karakter)
            
        karakter_markor.close()

    def slettResultat():
        karakter_markor = oblig2021database.cursor()

        studentnr = input_studnr.get()
        emne = input_emne.get()
        dato = input_dato.get()
        karakter = input_karakter.get()

        slett_sql = ('DELETE FROM Eksamensresultat WHERE Studentnr = %s AND Emnekode = %s AND Dato = %s AND Karakter = %s')
        data_slett = (studentnr,emne,dato,karakter)

        karakter_markor.execute(slett_sql,data_slett)
        oblig2021database.commit()

        input_studnr.set('')
        input_emne.set('')
        input_dato.set('')
        input_karakter.set('')

        karakter_markor.close()

    ## GUI ##
    # Labels
    lbl_slettResultat = Label(vinduSlettResultat,text = 'Slett eksamensresultat')
    lbl_slettResultat.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

    lbl_studnr = Label(vinduSlettResultat,text = 'Studentnr')
    lbl_studnr.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_emne = Label(vinduSlettResultat,text = 'Emnekode')
    lbl_emne.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_dato = Label(vinduSlettResultat,text = 'Dato')
    lbl_dato.grid(row = 3,column = 0, padx = 10, pady = 5, sticky = E)

    lbl_karakter = Label(vinduSlettResultat,text = 'Karakter')
    lbl_karakter.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = E)

    # Entryfelt
    input_studnr = StringVar()
    entry_studnr = Entry(vinduSlettResultat, width = 6, textvariable = input_studnr)
    entry_studnr.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    input_emne = StringVar()
    entry_emne = Entry(vinduSlettResultat,width = 7, textvariable = input_emne)
    entry_emne.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    input_dato = StringVar()
    entry_dato = Entry(vinduSlettResultat, width = 8,textvariable = input_dato)
    entry_dato.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    input_karakter = StringVar()
    entry_karakter = Entry(vinduSlettResultat, width = 1, state = 'readonly', textvariable = input_karakter)
    entry_karakter.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = W)

    # Buttons
    btn_sok = Button(vinduSlettResultat,text = 'Søk etter resultat', command = sokKarakter)
    btn_sok.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    btn_slettResultat = Button(vinduSlettResultat,width = 7,text = 'Slett', command = slettResultat)
    btn_slettResultat.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduSlettResultat,text = 'Tilbake til hovedvindu',command = vinduSlettResultat.destroy)
    btn_tilbake.grid(row = 7, column = 2, padx = 10, pady = 5, sticky = E)


def vinduEmneUtskrift():
    # F E R D I G
    vinduEmneUtskrift = Toplevel()
    vinduEmneUtskrift.title('Alle Studenter med besått eksamen i ett emne')

    def sokEksamen():

        for widget in vinduEmneUtskrift.winfo_children():
            widget.destroy()

        emne_sql = ("SELECT E.Studentnr,E.Emnekode,E.Dato,E.Karakter \
                    FROM Eksamensresultat AS E \
                    WHERE E.Emnekode = %s \
                        AND E.Karakter != %s \
                    GROUP BY E.Studentnr,E.Emnekode,E.Dato \
                    HAVING NOT E.Karakter > \
                        (SELECT E2.Karakter \
                        FROM Eksamensresultat AS E2 \
                        WHERE E.Studentnr = E2.Studentnr \
                        ORDER BY E2.Karakter ASC LIMIT 1) \
                    ORDER BY E.Studentnr")

        emne_markor = oblig2021database.cursor()
        
        emne = input_emne.get()
        lavestekarakter = 'F'
        emne_data = (emne,lavestekarakter)
        
        
        emne_markor = oblig2021database.cursor()
        emne_markor.execute(emne_sql,emne_data)


        emneliste = []
        emneliste += emne_markor

        emne_markor.close()

        lbl_studentnr = Label(vinduEmneUtskrift, text = 'Studentnr')
        lbl_studentnr.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)

        lbl_karakteroverskrift = Label(vinduEmneUtskrift, text = 'Karakter')
        lbl_karakteroverskrift.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)
        
        listelengde = len(emneliste)

        rad = 4
        listeteller = 0
        for row in range(listelengde):

            studnrset = StringVar()
            lbl_studnr = Label(vinduEmneUtskrift, textvariable = studnrset)
            lbl_studnr.grid(row = rad, column = 0, padx = 10, pady = 5, sticky = W)

            karakterset = StringVar()
            lbl_karakter = Label(vinduEmneUtskrift, textvariable = karakterset)
            lbl_karakter.grid(row = rad, column = 1, padx = 10, pady = 5, sticky = W)
            

            studnrset.set(emneliste[listeteller][0])
            karakterset.set(emneliste[listeteller][3])
            

            listeteller += 1
            rad += 1

        btn_tilbake = Button(vinduEmneUtskrift,text = 'Tilbake til hovedvindu',command = vinduEmneUtskrift.destroy)
        btn_tilbake.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = E)   
 
    ### GUI ##
    # Labels
    lbl_emneUtskrift = Label(vinduEmneUtskrift,text='Karakterutskrift for gjennomført eksamen i et emne')
    lbl_emneUtskrift.grid(row = 0, columnspan = 2, padx = 10, pady = 5, sticky = W)

    lbl_emne = Label(vinduEmneUtskrift, text='Emne')
    lbl_emne.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)


    # Entry felt
    input_emne = StringVar()
    ent_emne = Entry(vinduEmneUtskrift,width =7, textvariable = input_emne)
    ent_emne.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    # Knapper
    btn_sokEksamen = Button(vinduEmneUtskrift, text = 'Søk', command = sokEksamen)
    btn_sokEksamen.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduEmneUtskrift,text = 'Tilbake til hovedvindu',command = vinduEmneUtskrift.destroy)
    btn_tilbake.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = E)



def vinduKarakterUtskrift():
    # F E R D I G
    vinduKarakterUtskrift = Toplevel()
    vinduKarakterUtskrift.title('Karakterstatistikk for en eksamen')

    def sokKarakter():
        eksamen_markor = oblig2021database.cursor()

        emnekode = input_emne.get()
        dato = input_dato.get()

        eksamen_sql = ('SELECT Karakter FROM Eksamensresultat WHERE Emnekode = %s AND Dato = %s')
        eksamen_data = (emnekode,dato)

        eksamen_markor.execute(eksamen_sql,eksamen_data)

        karakterliste = []
        karakterliste += eksamen_markor

        eksamen_markor.close()

        listelengde = len(karakterliste)

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0

        for row in range(listelengde):
            if karakterliste[row][0] == 'A':
                a += 1
            elif karakterliste[row][0] == 'B':
                b += 1
            elif karakterliste[row][0] == 'C':
                c += 1
            elif karakterliste[row][0] == 'D':
                d += 1
            elif karakterliste[row][0] == 'E':
                e += 1
            elif karakterliste[row][0] == 'F':
                f += 1
        input_A.set(a)
        input_B.set(b)
        input_C.set(c)
        input_D.set(d)
        input_E.set(e)
        input_F.set(f)


    ## GUI ##
    # Labels
    lbl_karakterUtskrift = Label(vinduKarakterUtskrift,text = 'Karakterstatistikk')
    lbl_karakterUtskrift.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

    lbl_emne = Label(vinduKarakterUtskrift,text = 'Emne')
    lbl_emne.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = E)

    lbl_dato = Label(vinduKarakterUtskrift, text = 'Dato')
    lbl_dato.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = E)

    lbl_A = Label(vinduKarakterUtskrift, text = 'A :')
    lbl_A.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = E)

    lbl_B = Label(vinduKarakterUtskrift, text = 'B :')
    lbl_B.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = E)

    lbl_C = Label(vinduKarakterUtskrift, text = 'C :')
    lbl_C.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = E)
    
    lbl_D = Label(vinduKarakterUtskrift, text = 'D :')
    lbl_D.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = E)
    
    lbl_E = Label(vinduKarakterUtskrift, text = 'E :')
    lbl_E.grid(row = 8, column = 1, padx = 10, pady = 5, sticky = E)

    lbl_F = Label(vinduKarakterUtskrift, text = 'F :')
    lbl_F.grid(row = 9, column = 1, padx = 10, pady = 5, sticky = E)

    # Entry-felt
    input_emne = StringVar()
    entry_emne = Entry(vinduKarakterUtskrift,width = 7, textvariable = input_emne)
    entry_emne.grid(row = 1, column = 1, padx = 10, pady =5, sticky = W)

    input_dato = StringVar()
    entry_dato = Entry(vinduKarakterUtskrift,width = 8, textvariable = input_dato)
    entry_dato.grid(row = 2, column = 1, padx = 10, pady =5, sticky = W)

    input_A = StringVar()
    ent_A = Entry(vinduKarakterUtskrift,width=1,state = 'readonly', textvariable = input_A)
    ent_A.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = E)

    input_B = StringVar()
    ent_B = Entry(vinduKarakterUtskrift,width=1,state = 'readonly', textvariable = input_B)
    ent_B.grid(row = 5, column = 2, padx = 10, pady = 5, sticky = E)

    input_C = StringVar()
    ent_C = Entry(vinduKarakterUtskrift,width=1,state = 'readonly', textvariable = input_C)
    ent_C.grid(row = 6, column = 2, padx = 10, pady = 5, sticky = E)

    input_D = StringVar()
    ent_D = Entry(vinduKarakterUtskrift,width=1,state = 'readonly', textvariable = input_D)
    ent_D.grid(row = 7, column = 2, padx = 10, pady = 5, sticky = E)

    input_E = StringVar()
    ent_E = Entry(vinduKarakterUtskrift,width=1,state = 'readonly', textvariable = input_E)
    ent_E.grid(row = 8, column = 2, padx = 10, pady = 5, sticky = E)

    input_F = StringVar()
    ent_F = Entry(vinduKarakterUtskrift,width=1,state = 'readonly', textvariable = input_F)
    ent_F.grid(row = 9, column = 2, padx = 10, pady = 5, sticky = E)
    
    # Knapper
    btn_sok = Button(vinduKarakterUtskrift,text = 'Søk Eksamen', command = sokKarakter)
    btn_sok.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = E)

    btn_tilbake = Button(vinduKarakterUtskrift,text = 'Tilbake til hovedvindu',command = vinduKarakterUtskrift.destroy)
    btn_tilbake.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = E)

def vinduVitnemalUtskrift():
    # F E R D I G
    vinduVitnemalUtskrift = Toplevel()
    vinduVitnemalUtskrift.title('Vitnemålutskrift for en student')

    vitnemal_sql = ('SELECT Studentnr,Eksamensresultat.Emnekode,Emnenavn,MIN(Karakter),Studiepoeng \
                FROM Eksamensresultat,Emne \
                WHERE Eksamensresultat.Emnekode = Emne.Emnekode \
                    AND Studentnr = %s \
                GROUP BY Studentnr,Eksamensresultat.Emnekode,Emnenavn,Studiepoeng \
                ORDER BY SUBSTR(Eksamensresultat.Emnekode, -4) ASC')
    
    def sokStudnr():

        
        for widget in vinduVitnemalUtskrift.winfo_children():
            widget.destroy()

    
        vitnemal_markor = oblig2021database.cursor()
        studnr = input_studnr.get()

        vitnemal_data = (studnr,)

        vitnemal_markor.execute(vitnemal_sql,vitnemal_data)
        
        vitnemal_liste = []
        vitnemal_liste += vitnemal_markor

        navn_sql = ('SELECT Fornavn,Etternavn FROM Student WHERE Studentnr = %s')
        navn_data = (studnr,)
        vitnemal_markor.execute(navn_sql,navn_data)

        navn_liste = []
        navn_liste += vitnemal_markor

        vitnemal_markor.close()

        
        input_navn = StringVar()
        lbl_navn = Label(vinduVitnemalUtskrift, textvariable = input_navn)
        lbl_navn.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)
        
        if navn_liste:
            fornavn = navn_liste[0][0]
            etternavn = navn_liste[0][1]
            input_navn.set(fornavn + ' ' + etternavn)
        else:
            input_navn.set('Studenten eksisterer ikke.')

        listelengde = len(vitnemal_liste)

        # Diverse startverdier på tellere som kommer til bruk i for-lækken.
        poengsum = 0
        rad = 3
        emnekolonne = 0
        emnenavnkolonne = 1
        karakterkolonne = 2
        poengkolonne = 3

        listeteller = 0

        # Her opprettes alle labels og entrys for utskrift av karakterene til oppgitt student.
        for row in range(listelengde):
            # Emnekomponenter    
            emneset = StringVar()
            lbl_emne = Label(vinduVitnemalUtskrift,textvariable = emneset, width = 7)
            lbl_emne.grid(row = rad, column = emnekolonne, padx = 10, pady = 5, sticky = W)

            # Emnenavnkomponenter
            
            emnenavnset = StringVar()
            lbl_emnenavn = Label(vinduVitnemalUtskrift, textvariable = emnenavnset)
            lbl_emnenavn.grid(row = rad, column = emnenavnkolonne, padx = 10, pady = 5, sticky = W)

            # Karakterkomponenter
            
            karakterset = StringVar()
            lbl_karakter = Label(vinduVitnemalUtskrift, textvariable = karakterset, width = 2)
            lbl_karakter.grid(row = rad, column = karakterkolonne, padx = 10, pady = 5, sticky = W)

            # Poengkomponenter
            
            poengset = StringVar()
            lbl_poeng = Label(vinduVitnemalUtskrift, textvariable = poengset, width = 3)
            lbl_poeng.grid(row = rad, column = poengkolonne, padx = 10, pady = 5, sticky = W)
            
            

            emneset.set(vitnemal_liste[listeteller][1])
            emnenavnset.set(vitnemal_liste[listeteller][2])
            karakterset.set(vitnemal_liste[listeteller][3])

            # If-test for å se om karakteren er satt til F og får da 0 studiepoeng fra emnet.
            if vitnemal_liste[listeteller][3] == 'F':
                poengset.set(0)
            else:
                poengset.set(vitnemal_liste[listeteller][4])
                poengsum += vitnemal_liste[listeteller][4]
            
            # Tellere - Poengsum summeres, raden øker og listetelleren øker.
            rad = rad + 1
            listeteller = listeteller + 1

        rad += 1

        lbl_totalsum = Label(vinduVitnemalUtskrift, text = 'Total Poengsum:')
        lbl_totalsum.grid(row = rad, column = 2, padx = 10, pady = 5, sticky = E)
        
        totalpoengsum = StringVar()
        totalpoengsum.set(poengsum)
        entry_totalsum = Entry(vinduVitnemalUtskrift, width = 4,state = 'readonly', textvariable = totalpoengsum)
        entry_totalsum.grid(row = rad, column = 3, padx = 10, pady = 5, sticky = W)

        lbl_emnekode = Label(vinduVitnemalUtskrift,text = 'Emnekode')
        lbl_emnekode.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)

        lbl_emnenavn = Label(vinduVitnemalUtskrift,text = 'Emnenavn')
        lbl_emnenavn.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

        lbl_karakter = Label(vinduVitnemalUtskrift,text = 'Karakter')
        lbl_karakter.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)

        lbl_studiepoeng = Label(vinduVitnemalUtskrift,text = 'Studiepoeng')
        lbl_studiepoeng.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = W)


        btn_nullstill = Button(vinduVitnemalUtskrift, text = 'Tilbake til hovedvindu',command = vinduVitnemalUtskrift.destroy)
        btn_nullstill.grid(row= 0, column = 2, padx = 10, pady = 5, sticky = W)
        
        
    lbl_karakterUtskrift = Label(vinduVitnemalUtskrift,text = 'Karakterutskrift')
    lbl_karakterUtskrift.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)



    input_studnr = StringVar()
    entry_studnr = Entry(vinduVitnemalUtskrift, width = 6, textvariable = input_studnr)
    entry_studnr.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)


    btn_sokStudnr = Button(vinduVitnemalUtskrift, text = 'Søk studentnr', command = sokStudnr)
    btn_sokStudnr.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduVitnemalUtskrift,text = 'Tilbake til hovedvindu',command = vinduVitnemalUtskrift.destroy)
    btn_tilbake.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = E)


def vinduEksamenDag():
    # F E R D I G
    vinduEksamenDag = Toplevel()
    vinduEksamenDag.title('Eksamener på dato')

    def dagSok():

        for widget in vinduEksamenDag.winfo_children():
            widget.destroy()
            
        dag_markor = oblig2021database.cursor()

        dato = input_dato.get()

        dag_sql = ('SELECT Emnekode, Romnr FROM Eksamen WHERE Dato = %s')
        dag_data = (dato,)

        dag_markor.execute(dag_sql,dag_data)

        eksamenliste = []
        eksamenliste += dag_markor

        dag_markor.close()

        listelengde = len(eksamenliste)

        rad = 4
        for i in range(listelengde):
            emnevar = 'inputemne' + str(i)
            emnelabel = 'emne' + str(i)
            
            romvar = 'inputrom' + str(i)
            romlabel = 'rom' + str(i)

            emnevar = StringVar()
            emnevar.set(eksamenliste[i][0])
            emnelabel = Label(vinduEksamenDag, width = 7, textvariable = emnevar)
            emnelabel.grid(row = rad, column = 0, padx = 10, pady = 5, sticky = W)

            romvar = StringVar()
            romvar.set(eksamenliste[i][1])
            romlabel = Label(vinduEksamenDag,width = 4, textvariable = romvar)
            romlabel.grid(row = rad, column = 1, padx = 10, pady = 5, sticky = W)

            rad += 1

        lbl_emnekode = Label(vinduEksamenDag, text = 'Emnekode')
        lbl_emnekode.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)

        lbl_romnr = Label(vinduEksamenDag, text = 'Romnr')
        lbl_romnr.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)
        
        btn_nullstill = Button(vinduEksamenDag, text = 'Tilbake til hovedvindu',command = vinduEksamenDag.destroy)
        btn_nullstill.grid(row= 3, column = 2, padx = 10, pady = 5, sticky = W)
            

    ## GUI
    # Labels
    lbl_eksamenDag = Label(vinduEksamenDag,text='Eksamener på dato')
    lbl_eksamenDag.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

    lbl_dato = Label(vinduEksamenDag,text = 'Dato')
    lbl_dato.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    # Entrys
    input_dato = StringVar()
    entry_dato = Entry(vinduEksamenDag, width = 8, textvariable = input_dato)
    entry_dato.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    # Knapper
    btn_sok = Button(vinduEksamenDag, text = 'Søk', command = dagSok)
    btn_sok.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduEksamenDag,text = 'Tilbake til hovedvindu',command = vinduEksamenDag.destroy)
    btn_tilbake.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = E)


def vinduEksamenPeriode():
    # F E R D I G
    vinduEksamenPeriode = Toplevel()
    vinduEksamenPeriode.title('Eksamener i en periode')

    def periodeSok():

        for widget in vinduEksamenPeriode.winfo_children():
            widget.destroy()

        periode_markor = oblig2021database.cursor()

        fradato = input_fraDato.get()
        tildato = input_tilDato.get()

        periode_sql = ('SELECT * FROM Eksamen \
                        WHERE Dato >= %s AND Dato <= %s \
                        ORDER BY Dato')
        periode_data = (fradato,tildato)

        periode_markor.execute(periode_sql,periode_data)
        periode_markor.close()

        eksamenliste = []
        eksamenliste += periode_markor

        listelengde = len(eksamenliste)

        rad = 5
        widgetliste = []
        for i in range(listelengde):

            datovar = 'inputdato' + str(i)
            datolabel = 'dato' + str(i)

            widgetliste += [datolabel]
            
            emnevar = 'inputemne' + str(i)
            emnelabel = 'emne' + str(i)

            widgetliste +=[emnelabel]

            romvar = 'inputrom' + str(i)
            romlabel = 'rom' + str(i)

            widgetliste +=[romlabel]

            datovar = StringVar()
            datovar.set('')
            datovar.set(str(eksamenliste[i][1]))
            datolabel = Label(vinduEksamenPeriode,width = 10,textvariable = datovar)
            datolabel.grid(row = rad, column = 0, padx = 10, pady = 5, sticky = W)

            emnevar = StringVar()
            emnevar.set('')
            emnevar.set(eksamenliste[i][0])
            emnelabel = Label(vinduEksamenPeriode, width = 7, textvariable = emnevar)
            emnelabel.grid(row = rad, column = 1, padx = 10, pady = 5, sticky = W)

            romvar = StringVar()
            romvar.set('')
            romvar.set(eksamenliste[i][2])
            romlabel = Label(vinduEksamenPeriode, width = 4, textvariable = romvar)
            romlabel.grid(row = rad, column = 2, padx = 10, pady = 5, sticky = W)

            rad += 1


                
        lbl_dato = Label(vinduEksamenPeriode, text = 'Dato')
        lbl_dato.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = W)

        lbl_emnekode = Label(vinduEksamenPeriode, text = 'Emnekode')
        lbl_emnekode.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

        lbl_rom = Label(vinduEksamenPeriode, text = 'Romnr')
        lbl_rom.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = W)       


        btn_nullstill = Button(vinduEksamenPeriode, text = 'Tilbake til hovedvindu',command = vinduEksamenPeriode.destroy)
        btn_nullstill.grid(row= 3, column = 2, padx = 10, pady = 5, sticky = W)

            
        


                
                    
    ## GUI
    # Labels
    lbl_eksamenPeriode = Label(vinduEksamenPeriode,text = 'Eksamener i en periode')
    lbl_eksamenPeriode.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = E)

    lbl_fraDato = Label(vinduEksamenPeriode, text = 'Fra dato')
    lbl_fraDato.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_tilDato = Label(vinduEksamenPeriode, text = 'Til dato')
    lbl_tilDato.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = E)

    lbl_dato = Label(vinduEksamenPeriode, text = 'Dato')
    lbl_dato.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = W)

    lbl_emnekode = Label(vinduEksamenPeriode, text = 'Emnekode')
    lbl_emnekode.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

    lbl_rom = Label(vinduEksamenPeriode, text = 'Romnr')
    lbl_rom.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = W)

    # Entry
    input_fraDato = StringVar()
    entry_fraDato = Entry(vinduEksamenPeriode,width = 8, textvariable = input_fraDato)
    entry_fraDato.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    input_tilDato = StringVar()
    entry_tilDato = Entry(vinduEksamenPeriode,width = 8, textvariable = input_tilDato)
    entry_tilDato.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    # Knapper
    btn_sok = Button(vinduEksamenPeriode, text = 'Søk',command = periodeSok)
    btn_sok.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

    btn_tilbake = Button(vinduEksamenPeriode,text = 'Tilbake til hovedvindu',command = vinduEksamenPeriode.destroy)
    btn_tilbake.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = E)
    

def main():
    hovedvindu = Tk()
    hovedvindu.title('Studentadministrasjon - Meny')

    ## GUI ##
    # Komponenter som har med ajourhold av studenter å gjøre
    lbl_student = Label(hovedvindu,text='Student')
    lbl_student.grid(row=0,column = 0, padx = 10, pady = 5)

    btn_vinduRegistrerStudent = Button(hovedvindu,text='Registrer Student',command=vinduRegistrerStudent,width = 15)
    btn_vinduRegistrerStudent.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)

    btn_vinduOppdaterStudent = Button(hovedvindu,text='Endre Student',command=vinduOppdaterStudent,width = 15)
    btn_vinduOppdaterStudent.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)

    btn_vinduSlettStudent = Button(hovedvindu,text='Slett Student',command=vinduSlettStudent,width = 15)
    btn_vinduSlettStudent.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W,)

    # Komponenter som har med ajourhold av eksamener å gjøre
    lbl_eksamen = Label(hovedvindu,text='Eksamen')
    lbl_eksamen.grid(row = 0, column = 1, padx = 10, pady = 5)

    btn_vinduOpprettEksamen = Button(hovedvindu,text='Opprett Eksamen',command = vinduOpprettEksamen,width = 15)
    btn_vinduOpprettEksamen.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

    btn_vinduEndreEksamen = Button(hovedvindu,text='Endre Eksamen',command = vinduEndreEksamen,width = 15)
    btn_vinduEndreEksamen.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

    btn_vinduEndreEksamen = Button(hovedvindu,text='Slett Eksamen',command = vinduSlettEksamen,width = 15)
    btn_vinduEndreEksamen.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)


    # Komponenter som har med ajourhold av eksamensresultater å gjøre
    lbl_resultat = Label(hovedvindu,text='Eksamensresultat')
    lbl_resultat.grid(row = 0, column = 2, padx = 10, pady = 5)

    btn_vinduRegistrerResultat = Button(hovedvindu,text='Registrer Resultat', command = vinduRegistrerResultat,width = 15)
    btn_vinduRegistrerResultat.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)

    btn_vinduEndreResultat = Button(hovedvindu,text='Endre Resultat', command = vinduEndreResultat,width = 15)
    btn_vinduEndreResultat.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)

    btn_vinduEndreResultat = Button(hovedvindu,text='Slett Resultat', command = vinduSlettResultat,width = 15)
    btn_vinduEndreResultat.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = W)

    # Komponenter som har med karakterutskrift å gjøre
    lbl_karakterUtskrift = Label(hovedvindu,text = 'Karakterutskrift')
    lbl_karakterUtskrift.grid(row = 0, column = 3, padx = 10, pady = 5)

    btn_emneUtskrift = Button(hovedvindu,text = 'Emne', command = vinduEmneUtskrift,width = 15)
    btn_emneUtskrift.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = W)

    btn_karakterUtskrift = Button(hovedvindu,text = 'Karakterstatistikk',command = vinduKarakterUtskrift, width = 15)
    btn_karakterUtskrift.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = W)

    btn_VitnemålUtskrift = Button(hovedvindu, text = 'Vitnemålutskrift',command = vinduVitnemalUtskrift, width = 15)
    btn_VitnemålUtskrift.grid(row = 3, column = 3, padx = 10, pady = 5, sticky = W)

    # Komponenter for resterende funksjoner
    lbl_andreFunksjoner = Label(hovedvindu, text = 'Andre funksjoner')
    lbl_andreFunksjoner.grid(row = 0, column = 4, padx = 10, pady = 5, sticky = W)

    btn_eksamenDag = Button(hovedvindu,text = 'Se eksamener på dato', command = vinduEksamenDag)
    btn_eksamenDag.grid(row = 1, column = 4, padx = 10, pady = 5, sticky = W)

    btn_eksamenPeriode = Button(hovedvindu, text = 'Se eksamner periodevis', command = vinduEksamenPeriode)
    btn_eksamenPeriode.grid(row = 2, column = 4, padx = 10, pady = 5, sticky = W)
    
    
    

    hovedvindu.mainloop()


main()
    
