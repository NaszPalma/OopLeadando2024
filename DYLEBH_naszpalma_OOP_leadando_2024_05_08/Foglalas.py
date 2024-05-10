import datetime
from Szoba import Szoba
from Szoba import EgyagyasSzoba
from Szoba import KetagyasSzoba
class Foglalas():
    def __init__(self, szoba : Szoba, datum : datetime.date, fogl_nev : str):
        self.szoba = szoba
        self.datum = datum
        self.fogl_nev = fogl_nev
    def kiirva(self) ->str:
        kiirando = f"||szobaszám: {self.szoba.szobaSzam}, dátum: {self.datum}, Foglalási név: {self.fogl_nev}, szoba típúsa: "
        if isinstance(self.szoba, EgyagyasSzoba):
            kiirando = kiirando + "egy ágyas||"
        else:
            kiirando = kiirando + "két ágyas||"
        return kiirando