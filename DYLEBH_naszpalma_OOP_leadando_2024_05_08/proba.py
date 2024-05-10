#DYLEBH Nász Pálma 2024
import tkinter as tk
import datetime
from Szalloda import Szalloda
from Foglalas import Foglalas

def foglal_proba():
    if foglalas_e_szobaszam.get()=="" or foglalas_e_datum.get()=="" or foglalas_e_nev.get()=="":
        foglalas_hibauz.config(text="hibás kitöltés")
    else:
        datumm = datetime.date(int(foglalas_e_datum.get().split('-')[0]), int(foglalas_e_datum.get().split('-')[1]),
                               int(foglalas_e_datum.get().split('-')[2]))
        if datumm <= datetime.date.today():
            foglalas_hibauz.config(text="formátum/idő hiba")
        else:
            foglalas_hibauz.config(text=pelda_szalloda.foglalas(foglalas_e_szobaszam.get(),datumm,foglalas_e_nev.get()))
def torles_proba():
    if torles_e_szobaszam.get()=="" or torles_e_datum.get()=="":
        foglalas_hibauz.config(text="hibás kitöltés")
    else:
        datumm = datetime.date(int(torles_e_datum.get().split('-')[0]), int(torles_e_datum.get().split('-')[1]),
                               int(torles_e_datum.get().split('-')[2]))
        torles_hibauz.config(text=pelda_szalloda.foglalas_lemondas(torles_e_szobaszam.get(),datumm))
def frissit_lista():
    kilistazas_box.config(text=pelda_szalloda.foglalas_listazas())

pelda_szalloda = Szalloda("Rózsagóc Szálló","Mérges")
pelda_szalloda.szobafelvetel("11A",True, True)
pelda_szalloda.szobafelvetel("12B",False, False,23)
pelda_szalloda.szobafelvetel("21A",True, False)
#példa foglalások bekényszerítve, itt nincs ellenőrzés
pelda_szalloda.foglalasok.append(Foglalas(pelda_szalloda.szobak[0], datetime.date(2020, 5, 17), "Mézga Géza"))
pelda_szalloda.foglalasok.append(Foglalas(pelda_szalloda.szobak[1], datetime.date(2020, 5, 18), "Mézga Kriszta"))
pelda_szalloda.foglalasok.append(Foglalas(pelda_szalloda.szobak[0], datetime.date(2020, 5, 17), "Mézgáné Rezovits Paula"))
pelda_szalloda.foglalasok.append(Foglalas(pelda_szalloda.szobak[2], datetime.date(2020, 5, 11), "Dr. Máris"))
pelda_szalloda.foglalasok.append(Foglalas(pelda_szalloda.szobak[0], datetime.date(2020, 6, 19), "Hufnágel Pisti"))
window = tk.Tk()
window.title("Szálloda")
window.geometry("350x700")
# lapelemek
menu_1_label = tk.Label(window, text="Foglalás", font=('Arial', 20))
menu_1_label.grid(row=0, column = 0, columnspan =2)
# foglalas kitoltes
foglalas_l_szobaszam = tk.Label(window, text="Szobaszám:", font=('Arial', 12))
foglalas_l_szobaszam.grid(row=1, column = 0)
foglalas_e_szobaszam = tk.Entry()
foglalas_e_szobaszam.grid(row=1, column = 1)

foglalas_l_datum = tk.Label(window, text="Dátum (pl.: 2024-5-17):", font=('Arial', 12))
foglalas_l_datum.grid(row=2, column = 0)
foglalas_e_datum = tk.Entry()
foglalas_e_datum.grid(row=2, column = 1)

foglalas_l_nev = tk.Label(window, text="milyen néven szeretné foglalni?", font=('Arial', 12))
foglalas_l_nev.grid(row=3, column = 0)
foglalas_e_nev = tk.Entry()
foglalas_e_nev.grid(row=3, column = 1)

foglalas_gomb = tk.Button(window, text="Foglalás",font=('Arial', 12), command=foglal_proba)
foglalas_gomb.grid(row=4, column = 0)
foglalas_hibauz = tk.Label(window, text="####", font=('Arial', 12))
foglalas_hibauz.grid(row=4, column = 1)
# torles kitoltes
menu_2_label = tk.Label(window, text="Foglalás törlése", font=('Arial', 20))
menu_2_label.grid(row=5, column = 0, columnspan =2)

torles_l_szobaszam = tk.Label(window, text="Szobaszám:", font=('Arial', 12))
torles_l_szobaszam.grid(row=6, column = 0)
torles_e_szobaszam = tk.Entry()
torles_e_szobaszam.grid(row=6, column = 1)

torles_l_datum = tk.Label(window, text="Dátum (pl.: 2024-5-17):", font=('Arial', 12))
torles_l_datum.grid(row=7, column = 0)
torles_e_datum = tk.Entry()
torles_e_datum.grid(row=7, column = 1)

torles_gomb = tk.Button(window, text="Törlés",font=('Arial', 12), command=torles_proba)
torles_gomb.grid(row=8, column = 0)
torles_hibauz = tk.Label(window, text="####", font=('Arial', 12))
torles_hibauz.grid(row=8, column = 1)
# kilistázás
menu_3_label = tk.Label(window, text="Kilistázás", font=('Arial', 20))
menu_3_label.grid(row=9, column = 0, columnspan =2)
lista_gomb = tk.Button(window, text="Frissítés",font=('Arial', 12), command=frissit_lista)
lista_gomb.grid(row=10, column = 0, columnspan =2)

kilistazas_box = tk.Message(window,font=('Arial', 10))
kilistazas_box.config(text = pelda_szalloda.foglalas_listazas())
kilistazas_box.grid(row=11, column = 0, columnspan =2)
# lapelemek vége
window.mainloop()
