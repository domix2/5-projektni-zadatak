from korisnik import ispis_korisnika
from artikl import ispis_artikla

class Prodaja:
    def __init__(self, datum, korisnik, artikl):
        self.datum = datum
        self.korisnik = korisnik
        self.artikl = artikl

    def ispis(self):
        self.korisnik.ispis()
        self.artikl.ispis()
        print('Datum isteka:')
        print(f"\tDan: {self.datum.day}")
        print(f"\tMjesec: {self.datum.month}")
        print(f"\tGodina: {self.datum.year}")
        print('-' * 20)