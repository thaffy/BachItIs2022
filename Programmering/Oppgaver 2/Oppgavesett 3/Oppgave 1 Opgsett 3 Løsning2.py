
student=[]
ny_student=True

while ny_student==True:
    studentnr=input('Oppgi studentnr: ')
    student +=[studentnr]
    fornavn=input('Oppgi fornavn: ')
    student +=[fornavn]
    studium=input('Oppgi studium: ')
    student +=[studium]
    

    svar=input('Skal det leses inn flere fornavn? (ja/nei) ')
    if svar=='nei':
        ny_student=False
        
print('Listen du har skrevet inn er:')
print(student)

# step skal være 3

listelengde=len(fornavn)
    
