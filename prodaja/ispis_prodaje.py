from korisnik import ispis_korisnika
from artikl import ispis_artikla

def ispis_prodaje(prodaja):
    ispis_korisnika(prodaja['korisnik'])
    ispis_artikla(prodaja['artikl'])
    print('Datum isteka:')
    print(f"\tDan: {prodaja['datum'].day}")
    print(f"\tMjesec: {prodaja['datum'].month}")
    print(f"\tGodina: {prodaja['datum'].year}")
    print('-'*20)
def ispis_svih_prodaja(prodaje):
    print('Ispis svih prodaja:')
    for prodaja in prodaje:
        ispis_prodaje(prodaja)
