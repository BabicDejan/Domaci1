from json_formatiranje import Handling
from klasa_student import Student
from predmeti import Predmet

#manuelno dodavanje necu obradjivati unos, vec cu preko gui-a demonstrirati
'''student = Student("Dejan Babic", "18/019", "FIST")
print(student.__string__())


predmet = Predmet(student,"Matematika",5)
predmet1 = Predmet(student,"Matematika",5)



student2=Student("Tamara Pavlovic", "18/012", "FIST","8","osnovne")

predmet = Predmet(student2,"Infor",4)

handle = Handling(student)
handle1 = Handling(student2)
handle.napravi_json()
handle1.napravi_json()

 


#sad koristimo metodu pripreme preko bilo kojeg objekta tipa handle
#ovo je isto nepotrebno ali opet se trudim da OOP koristim

handle.pripremi()
handle.napravi_json()
handle1.napravi_json()
handle.zavrsi()
handle.sredi_json()

handle.obrisi_zagradu()
handle.upisi_zarez()
handle.napravi_json()
handle.zavrsi()
handle.sredi_json()'''

student = Student("Dejan Babic","18/019","FIST")
student._set_lista([["matematika",10]])


handle = Handling(student)
print(student.__string__())
handle.obrisi_zagradu()
handle.upisi_zarez()
handle.napravi_json()
handle.zavrsi()
handle.sredi_json()

