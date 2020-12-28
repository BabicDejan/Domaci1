from klasa_student import Student
#logika je malo poremecena, ali zelim da demonstriram OOP i demonstriram njhovu uvezanost
#zelim da vezem studenta za svaki objekat "predmet" ---> veza student 1 na vise predmeta (besmislena lista koja prikazuje da svaki student ima svoju listu), lista predmeta ce biti vezana za trazenog studenta samo
class Predmet(Student):
    #proslijedjujem konstruktoru objekat student, i u super inicijatoru koristim getere
    def __init__(self,objekat_student, ime_predmeta, ocjena):
        #u super konstruktoru pozivam i funkciju za povecanje broja predmeta kod studenta, ovim se postize jednostavnost racunannja broja predmeta koje student ima
        #sto znaci da mogu da koristim automatski broj predmeta za racunanje prosjeka studenta :D
        super().__init__(objekat_student.get_ime(),objekat_student.get_broj_indeksa(),objekat_student.get_fakultet(),objekat_student.povecaj_broj_predmeta(1),objekat_student._dodaj_predmet_ocjenu(ime_predmeta,ocjena))
        self.ime_predmeta=ime_predmeta
        self.ocjena=ocjena
#geteri
    def get_predmet(self):
        return self.ime_predmeta
    def get_ocjena(self):
        return self.ocjena
    def get_broj_predmeta(self):
        return self.broj_predmeta
#seteri
    def set_predmet(self,predmet):
        self.ime_predmeta=predmet
    def set_ocjena(self,ocjena):
        self.ocjena=ocjena
#>>>geteri od supera, samo za neke>>>
    def get_ime(self):
        return super().get_ime()
#valjace mi i broj indeksa ako zelim da racunam prosjek 
    def get_broj_indeksa(self):
        return super().get_broj_indeksa()
