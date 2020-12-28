class Student:
    def __init__(self,ime_studenta="", broj_indeksa="", fakultet="", broj_predmeta=0,lista_predmeta=[],prosjek=0):
        self.broj_predmeta = 0
        self.lista_predmeta = []
        self.ime_studenta=ime_studenta
        self.broj_indeksa=broj_indeksa
        self.fakultet=fakultet
        self.prosjek=prosjek
#geteri
    def get_ime(self):
        return self.ime_studenta
    def get_broj_indeksa(self):
        return self.broj_indeksa
    def get_fakultet(self):
        return self.fakultet
    def get_prosjek(self):
        return self.prosjek
#seteri
    def set_ime(self,ime):
        self.ime_studenta=ime
    def set_broj_indeksa(self,broj_indeksa):
        self.broj_indeksa=broj_indeksa
    def set_fakultet(self,fakultet):
        self.fakultet=fakultet
    #ovo setovanje ce mi trebati kod super konstruktora u json_formatiranje
    def _set_broj_predmeta(self,broj_predmeta):
        self.broj_predmeta=broj_predmeta
    def _set_lista(self,lista_predmeta):
        self.lista_predmeta=lista_predmeta[:]
    def set_prosjek(self,prosjek):
        self.prosjek=prosjek
#broj predmeta za studenta
    def povecaj_broj_predmeta(self,num):
        self.broj_predmeta+=num
    def get_broj_predmeta(self):
        return self.broj_predmeta

    def __string__(self):
        return self.ime_studenta+" "+self.broj_indeksa
#funkcija koja se moze koristiti na nivou klase (protected) a to je dodavanje predmeta i ocjene kao torke listi predmeta studenta kao nadklase
    def _dodaj_predmet_ocjenu(self,ime_predmeta,ocjena):
        self.lista_predmeta.append((ime_predmeta,ocjena))
#izlistati predmete studenta
    def izlistaj_predmete(self):
        #nacin predstavlja sta funkcija vrace, ako stavimo bilo sta drugo kao argument vratice samo listu predmeta ukoliko zelimo da stampamo nesto na ovaj nacin
        '''if nacin==0:
            print("Za ime i broj indeksa studenta:" + self.get_ime() + " " + self.get_broj_indeksa())
            print("")
            #formatiranje za crticu po sredini :'D
            spejs="      "
            print("Predmet"+spejs+"|"+"  "+"Ocjena")
            print("\n")
            for predmet,ocjena in self.lista_predmeta:
                if len("predmet")<len(predmet):
                    spejs=spejs[0:len(predmet)-len("predmet")]
                else:
                    spejs=spejs.ljust(len("predmet")-len(predmet)," ")
                print(f"{predmet}{spejs}|{spejs}{ocjena}")'''
        return self.lista_predmeta
#posto smo child klasi proslijedili dodavanje predmeta u listu, u vidu ocjene predmet, mozemo i da racunamo prosjek, prosjek se racuna samo na osnovu broja predmeta i ocjena, funkcija se prilagodjava nacinu racunanja prosjeka
#izracunaj prosjek studenta
    def izracunaj_prosjek(self):
        sabir=0
        for element in self.lista_predmeta:
            sabir = sabir+int(element[1])
        try:
            return float(sabir/self.get_broj_predmeta())
        except ZeroDivisionError:
            return 0