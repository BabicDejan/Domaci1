import json
from klasa_student import Student
# ova klasa ce da bude potklasa klase student i ona ce da hendluje upisivanje studenta u txt fajl, kao i citanje studenta iz txt fajla, format ce biti json
class Handling(Student):
    #ukoliko ne proslijedimo konstruktoru nista stavljamo None, moze sluziti kao operacija nad json-om
    def __init__(self,objekat_student=""):
        if isinstance(objekat_student,Student):
            super().__init__(objekat_student.get_ime(),objekat_student.get_broj_indeksa(),objekat_student.get_fakultet(),objekat_student.get_broj_predmeta(),objekat_student.izlistaj_predmete(),objekat_student.get_prosjek)
            #ovo se iskomplikovalo jer roditeljska klasa u konstruktoru broj predmeta stavlja na 0 i listu [] tako da sam morao ubaciti setere za njih
            super()._set_broj_predmeta(objekat_student.get_broj_predmeta())
            super()._set_lista(objekat_student.izlistaj_predmete())
            super().set_prosjek(objekat_student.get_prosjek())
        else:
            pass
    #funkcija za prebacanje sadrzaja studenta u dictionary koji cemo posle pretvoriti u json, i nakon toga upisati u txt
    #super geteri
    def get_ime(self):
        return super().get_ime()
    def get_broj_indeksa(self):
        return super().get_broj_indeksa()
    def get_fakultet(self):
        return super().get_fakultet()
    #opet nidje veze, ali zbog OOP
    def napravi_json(self):
        dictionary = {
            "Ime":self.get_ime(),
            "Br.Indeksa":self.get_broj_indeksa(),
            "Fakultet":self.get_fakultet(),
            "Predmet_ocjena":super().izlistaj_predmete(),
            "Prosjek":super().izracunaj_prosjek()
        }
        with open ('json_studenti.json','a') as studenti:
            studenti.write("[")
            json.dump(dictionary,studenti,indent=1)
            studenti.write("]")
            studenti.write("\n")
            studenti.write(",")
            studenti.write("\n")
    #odje dodajemo manuelno u JSON, svaki put kada zelimo da manuelno dodamo, moramo obratiti paznju da obrisemo fajl
    #ovdje upisujemo pocetak fajla, jer cemo imati vise objekata u njemu tipa JSON, a parser json.load() 
    #moze samo ucitati jedan objekat json, pa cemo mu mi na ovaj nacin proslijediti jednu listu svih JSON objekata koju ce on tretirati kao 1
    #pripremi pozivamo kad ne postoji fajl .JSON iliti kada ga obrisemo
    def pripremi(self):
        with open('json_studenti.json', 'w') as fajl:
            fajl.seek(0)
            fajl.write("[")
    #ovu pozivamo kada je upisivanje zavrseno
    def zavrsi(self):
        with open('json_studenti.json','a') as fajl:
            fajl.write("]")
    #metoda napravi_json() dodaje "," na kraj svake linije, da bi mogli imati red u listi, pa po zavrsetku unosenja studenata imamo visak "," tako da cemo ih maknuti   
    def sredi_json(self):
        with open('json_studenti.json',"r") as fajl:
            lines = fajl.readlines()
            fajl.close()
        if lines[len(lines)-2].strip("\n") == ",":
            del lines[len(lines)-2]
        else:
            pass
        with open('json_studenti.json',"w+") as fajl:
            fajl.seek(0)
            for linija in lines:
                fajl.write(linija)
    #ovo je sve moglo u jednu metodu
    #brisanje poslednje "]" kako bi mogli unijeti novog
    def obrisi_zagradu(self):
        with open('json_studenti.json','r') as fajl:
            lines = fajl.readlines()
            fajl.close()
        if lines[len(lines)-1] == "]":
            del lines[len(lines)-1]
        else:
            pass
        with open('json_studenti.json',"w") as fajl:
            fajl.seek(0)
            for linija in lines:
                fajl.write(linija)
        
    #ako json nije empty, kada dodajemo novi, moramo imati zarez na kraju
    def upisi_zarez(self):
        with open('json_studenti.json','a') as fajl:
            fajl.write(",")
            fajl.write("\n")
    