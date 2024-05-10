from abc import ABC

class Szoba(ABC):
    def __init__(self, szobaszam):
        self.ar = 0
        self.szobaSzam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, teljes_ellatas = False):
        super().__init__(szobaszam)
        self.ar = 40000
        self.teljesEll = teljes_ellatas
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, negyzetmeter = 25):
        super().__init__(szobaszam)
        self.ar = 60000
        self.negyzetmeter = negyzetmeter