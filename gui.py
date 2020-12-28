from tkinter import *
from json_formatiranje import Handling
from klasa_student import Student
from predmeti import Predmet
from tkinter import messagebox 
import json
import os
prozor = Tk()
prozor.title("Studenti Admin panel")
prozor.geometry("1000x800")

#URADITI:
#listbox za studente
#prvo obrada json fajla, kako bi ih mogli staviti u listu 
#klikom na element(student) liste, prikazuju se njegovi predmeti i ocjene u drugoj listi
#mogucnost dodavanja studenta i predmeta
#kada se student doda, upisuje se u json fajl, koji se svaki put obradjuje na pokretanju aplikacije
frame1 = Frame(prozor,width=250,height=400).grid(row=0,column=0,columnspan=1,rowspan=5)
frame2 = Frame(prozor,width=250,height=400).grid(row=0,column=2,columnspan=1,rowspan=5)
frame3 = Frame(prozor,width=250,height=400).grid(row=0,column=4,columnspan=1,rowspan=8)
frame4 = Frame(prozor,width=250,height=400).grid(row=4,column=0,columnspan=1,rowspan=4)
frame5 = Frame(prozor).grid(row=5,column=2,columnspan=1,rowspan=2)
frame6 = Frame(prozor).grid(row=5,column=3,columnspan=1,rowspan=2)

#LISTBOX ZA STUDENTE
# 1. obrada json fajla - baze
#provjeravamo da li je prazan JSON fajl, ukoliko nije prolazimo kroz njega i ubacamo elemente liste
if os.stat("json_studenti.json") != 0:
    #prvo moramo srediti json, odnosno provjeriti ima li (ono ",") i ukoliko ima metoda svoje zavrsava
    json_handle = Handling()
    #u metodi je direktno postavljeno ime fajla, naravno to je lako implementirati
    json_handle.sredi_json()
    #nakon sredjivanja, nema greske i sad prolazimo kroz fajl i stavljamo objekte u liste objekata studenata
    lista_objekata=[]
    with open("json_studenti.json","r") as studenti:
        json_content = json.load(studenti)
    for element in json_content:
        objekat_student = Student()
        #trenutno smo u elementu koji je lista, treba da se nadjemo u dict
        for ele in element:
            objekat_student.set_ime(ele["Ime"])
            objekat_student.set_broj_indeksa(ele["Br.Indeksa"])
            objekat_student.set_fakultet(ele["Fakultet"])
            objekat_student._set_lista(ele["Predmet_ocjena"])
            objekat_student.set_prosjek(ele["Prosjek"])
        lista_objekata.append(objekat_student)
else:
    pass
#konacno listbox
list_box_studenti = Listbox(frame1)
list_box_studenti.grid(row=0,column=2,padx=5,pady=5,sticky='nsew',rowspan=4)
list_box_predmeti = Listbox(frame3)
list_box_predmeti.grid(row=0,column=3,padx=5,pady=5,sticky="nsew",rowspan=4)
#lijepi na listbox sve objekte
for objekat in lista_objekata:
    list_box_studenti.insert(END,objekat.__string__())
#sada pravimo dugme koje cemo vezati za drugi linkbox koji ce nam pokazivati predmete studenta
def select():
    #po indeksu provjeravamo da li smo izabrali dobar objekat
    print(list_box_studenti.get(list_box_studenti.curselection()))
    indeks  = list_box_studenti.get(list_box_studenti.curselection()).split()
    print(indeks)
    for objekat in lista_objekata:
        if indeks[2]==objekat.get_broj_indeksa():
            labela_ime.config(text=objekat.get_ime())
            labela_indeks.config(text=objekat.get_broj_indeksa())
            labela_fakultet.config(text=objekat.get_fakultet())
            labela_prosjek.config(text=objekat.get_prosjek())
            list_box_predmeti.delete(0,"end")
            lista = objekat.izlistaj_predmete()
            for ele in lista:
                list_box_predmeti.insert(END,ele)
            break
dugme_select = Button(prozor, text="Pregledaj studenta", command = select)
dugme_select.grid(row=4,column=2,padx=2,pady=2)

labela_nam = Label(frame1,text="Ime:",width=10)
labela_nam.grid(row=0,column=0,columnspan=1)
labela_inde = Label(frame1,text="Br. Indeksa:",width=10)
labela_inde.grid(row=1,column=0,columnspan=1)
labela_fak = Label(frame1,text="Fakultet:",width=10)
labela_fak.grid(row=2,column=0,columnspan=1)
labela_pro= Label(frame1,text="Prosjek:",width=10)
labela_pro.grid(row=3,column=0,columnspan=1)


labela_ime = Label(frame1,text="",width=15)
labela_ime.grid(row=0,column=1,columnspan=1)
labela_indeks = Label(frame1,text="",width=15)
labela_indeks.grid(row=1,column=1,columnspan=1)
labela_fakultet = Label(frame1,text="",width=15)
labela_fakultet.grid(row=2,column=1,columnspan=1)
labela_prosjek= Label(frame1,text="",width=15)
labela_prosjek.grid(row=3,column=1,columnspan=1)

#dodavanje studenta
labela_unos_ime = Label(frame4,text="Unesite Ime:",width=12)
labela_unos_ime.grid(row=5,column=0,columnspan=1)
labela_unos_indeks = Label(frame4,text="Unesite index:",width=12)
labela_unos_indeks.grid(row=6,column=0,columnspan=1)
labela_unos_faks = Label(frame4,text="Unesite faks:",width=12)
labela_unos_faks.grid(row=7,column=0,columnspan=1)
#entry 
ime_entry = Entry(frame4,width=15)
ime_entry.grid(row=5,column=1)
indeks_entry = Entry(frame4,width=15)
indeks_entry.grid(row=6,column=1)
faks_entry = Entry(frame4,width=15)
faks_entry.grid(row=7,column=1)
#dodavanje predmeta studentu trenutnom
labela_predmet = Label(frame5,text="Predmet",width=12)
labela_predmet.grid(row=5,column=2,columnspan=1)
labela_ocjena = Label(frame5,text="Ocjena",width=12)
labela_ocjena.grid(row=6,column=2,columnspan=1)
#entry
predmet_entry = Entry(frame6,width=12)
predmet_entry.grid(row=5,column=3,sticky="w")

ocjena_entry = Entry(frame6,width=12)
ocjena_entry.grid(row=6,column=3,sticky="w")

#za svakog posebno validiramo i provjeravamo format
lista_predmeta=[]
def dodaj_predmet():
    predmet = predmet_entry.get()
    ocjena= ocjena_entry.get()
    try:
        predmet = str(predmet)
        if predmet.isdigit() or len(predmet)==0:
            messagebox.showwarning("Nepravilan unos imena fakulteta")
            predmet_entry.delete(0,"end")
            return
    except ValueError:
        messagebox.showwarning("Greska prilikom unosa")
        predmet_entry.delete(0,"end")
        return
    try:
        ocjena = int(ocjena)
        if ocjena<1 or ocjena>10:
            messagebox.showwarning("Ocjena ne moze biti ispod 1 i preko 10")
            ocjena_entry.delete(0,"end")
            return
    except ValueError:
        messagebox.showwarning("Ocjena ne moze biti rijec")
        ocjena_entry.delete(0,"end")
        return
    global lista_predmeta
    lista_predmeta.append([predmet,ocjena])
    predmet_entry.delete(0,"end")
    ocjena_entry.delete(0,"end")

def dodaj():
    student = Student()
    ime = ime_entry.get()
    indeks = indeks_entry.get()
    fakultet = faks_entry.get()
    #prvo ocu da vidim da li su predmet i ocjena, prazni i ukoliko je lista predmeta za studenta prazna da pitam da li zeli da kreira studenta bez predmeta
    #ostavljam sredjivanje tog problema za drugi put, manipulacija sa JSONOM i dodavanje preko listbox-a, ima posla, zasad ce svakom studentu morati predmet da se doda ovako
    #dakle prvo stavljamo koliko god predmeta zelimo, i onda kreiramo studenta koji ce imati te predmete 
    global lista_predmeta
    if len(lista_predmeta)==0:
        msg = messagebox.askquestion("Dodaj studenta", "Da li zelite da kreirate studenta bez predmeta?")
        if msg=="yes":
            pass
        else:
            return
    try:
        ime = str(ime)
        split = ime.split()
        if len(split)!=2 or ime.isdigit() or len(ime)==0:
            messagebox.showwarning("Morate unijeti ime i prezime")
            ime_entry.delete(0,"end")
            return
        else:
            pass
        for char in ime:
            if char.isdigit():
                messagebox.showwarning("Ime ne moze sadrzati brojeve")
                ime_entry.delete(0,"end")
                return
            else:
                student.set_ime(ime)
    except ValueError:
        messagebox.showwarning("Pogresno unijeto ime")
        ime_entry.delete(0,"end")
        return
    try:
        indeks = str(indeks)
        if len(indeks)==0 or indeks[2]!="/" or len(indeks)!=6 or int(indeks[3:])>20:
            messagebox.showwarning("Format indeksa nije dobro unesen! Format mora biti broj/<=trenutnaGodina")
            indeks_entry.delete(0,"end")
            return
        else:
            student.set_broj_indeksa(indeks)
    except ValueError:
        messagebox.showwarning("Format indeksa nije dobro unesen! Format mora biti broj/godina")
        indeks_entry.delete(0,"end")
        return
    try:
        fakultet = str(fakultet)
        if fakultet.isdigit() or len(fakultet)==0:
            messagebox.showwarning("Ime fakulteta ne mogu biti samo brojevi")
            faks_entry.delete(0,"end")
            return
        else:
            student.set_fakultet(fakultet)
    except ValueError:
        messagebox.showwarning("Greska prilikom unosa")
        faks_entry.delete(0,"end")
        return
    ime_entry.delete(0,"end")
    indeks_entry.delete(0,"end")
    faks_entry.delete(0,"end")
    #dodavanje liste predmeta na kraj
    student._set_lista(lista_predmeta)
    student._set_broj_predmeta(len(lista_predmeta))
    student.set_prosjek(student.izracunaj_prosjek())
    handl = Handling(student)

    lista_objekata.append(student)
    if os.stat("json_studenti.json") == 0:
        handl.pripremi()
        handl.napravi_json()
        handl.zavrsi()
        handl.sredi_json()
    else:
        handl.obrisi_zagradu()
        handl.upisi_zarez()
        handl.napravi_json()
        handl.zavrsi()
        handl.sredi_json()
    list_box_studenti.insert(END,student.__string__())
    lista_predmeta=[]
    messagebox.showinfo("Student kreiran")



dugme_predmet = Button(frame6, text="Dodaj predmet u listu", command = dodaj_predmet)
dugme_predmet.grid(row=7,column=2,columnspan=2)

dugme_dodaj_studenta = Button(frame4, text = "Dodaj studenta",command = dodaj,width=20)
dugme_dodaj_studenta.grid(row=10,column=0,columnspan=2)

prozor.mainloop()
    


