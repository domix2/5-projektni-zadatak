from datetime import date
from artikl import get_artikl
from korisnik import get_korisnik
from kategorija import get_kategorija

def unos_prodaje(korisnici, kategorije, redni_broj):

    prodaja = {}
    dan = int(input(f'Unesite dan isteka {redni_broj}. prodaje:'))
    mjesec = int(input(f'Unesite mjesec {redni_broj}. prodaje:'))
    godina = int(input(f'Unesite godinu {redni_broj}. prodaje:'))
    prodaja['datum'] = date(godina, mjesec, dan)

    print(f'Odaberite korisnika {redni_broj}. prodaje:')

    for i, korisnik in enumerate(korisnici, start=1):
        print(get_korisnik(i, korisnik))

    odabrani_korisnik = int(input("Odaberi korisnika: "))-1

    print(f"Odaberite kategoriju {redni_broj}. prodaje:")
    for i, artikl in enumerate(kategorije, start=1):
        print(get_kategorija(i, kategorije))

    odabrana_kategorija = int(input("Odabrana kategorija:")) - 1

    print(f"Odaberite artikl {redni_broj}. prodaje:")
    for i,artikl in enumerate(kategorije[odabrana_kategorija]['artikli'], start=1):
        print(get_artikl(i, artikl))

    odabrani_artikl = int(input("Odabrani artikl:"))-1

    prodaja['artikl'] = kategorije[odabrana_kategorija]['artikli'][odabrani_artikl]
    prodaja['korisnik'] = korisnici[odabrani_korisnik]
    return prodaja

