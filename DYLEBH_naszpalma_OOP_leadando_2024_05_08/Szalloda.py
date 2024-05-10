import datetime
from Foglalas import Foglalas
from Szoba import Szoba
from Szoba import EgyagyasSzoba
from Szoba import KetagyasSzoba
class Szalloda():
    def __init__(self, nev, telepules):
        self.nev = nev
        self.telepules = telepules
        self.szobak = []
        self.foglalasok = []
    def szobafelvetel(self, szobaszam, egyagyas : bool, teljes_ellatas : bool = False, negyzetmeter : int = 25):
        if egyagyas:
            self.szobak.append(EgyagyasSzoba(szobaszam, teljes_ellatas))
        else:
            self.szobak.append(KetagyasSzoba(szobaszam,negyzetmeter))
    def foglalas(self, szobaszam, datum : datetime.date, foglalasi_nev) -> str:
        szobam = None
        valid_szoba = False
        for szoba_epp in self.szobak:
            if szoba_epp.szobaSzam == szobaszam:
                valid_szoba = True
                szobam = szoba_epp
                break
        if valid_szoba:
            for fogl in self.foglalasok:
                if fogl.szoba.szobaSzam==szobaszam and fogl.datum == datum:
                    valid_szoba = False
                    break
        if valid_szoba:
            self.foglalasok.append(Foglalas(szobam, datum, foglalasi_nev))
            return f"Sikeres foglalás, {datum} dátumon, {foglalasi_nev} néven, a {szobaszam} számú szobába\n A szoba ára: {szobam.ar}"
        else:
            return "Az adott dátumon, ilyen szobaszámmal, nincs szabad időszak. A foglalás nem lehetséges."
    def foglalas_lemondas(self, szobaszam, datum : datetime.date) ->str:
        for i in range(len(self.foglalasok)):
            if self.foglalasok[i].szoba.szobaSzam == szobaszam and self.foglalasok[i].datum == datum:
                self.foglalasok.pop(i)
                return "A foglalás törölve lett."
        return "Nem találtunk foglalást ezekkel a paraméterekkel"
    def foglalas_listazas(self) -> str:
        kiirando = ""
        for fogl in self.foglalasok:
            kiirando = kiirando + fogl.kiirva() + "\n"
        return kiirando