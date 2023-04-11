from artikl import ispis_artikla
from korisnik import ispis_korisnika

def ispis_prodaje(prodaja):
    ispis_korisnika(prodaja['korisnik'])
    ispis_artikla(prodaja['artikl'])
    print("Datum isteka:")
    print(f"\tDan: {prodaja['datum'].day}")
    print(f"\tMjesec: {prodaja['datum'].month}")
    print(f"\tGodina: {prodaja['datum'].year}")
    print('-'*20)
