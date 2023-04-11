from artikl import get_artikl
from korisnik import get_korisnik
from kategorija import get_kategorija
from datetime import date

def unos_prodaje(korisnici, kategorije, redni_broj):
    prodaja={}
    dan = int(input(f"Unesite dan isteka {redni_broj}. prodaje:"))
    mjesec = int(input(f"Unesite mjesec isteka {redni_broj}. prodaje:"))
    godina = int(input(f"Unesite godinu isteka {redni_broj}. prodaje:"))
    prodaja['datum'] = date(godina, mjesec, dan)

    print(f"Odaberite korisnika {redni_broj}. prodaje")
    for i, korisnik in enumerate(korisnici, start=1):
        print(get_korisnik(i, korisnik))

    odabrani_korisnik = int(input("Odabrani korisnik:"))
    prodaja['korisnik'] = korisnici[odabrani_korisnik-1]

    print(f"Odaberite kategoriju {redni_broj}. prodaje")
    for i, kategorija in enumerate(kategorije, start=1):
        print(get_kategorija(i, kategorija))

    odabrana_kategorija = int(input("Odabrana kategorija:"))

    print(f"Odaberite artikl {redni_broj}. prodaje")
    for i, artikl in enumerate(kategorije[odabrana_kategorija -1]['artikli'], start=1):
        print(get_artikl(i, artikl))

    odabrani_artikl = int(input("Odabrani artikl:"))
    prodaja['artikl'] = kategorije[odabrana_kategorija -1]['artikli'][odabrani_artikl -1]
    return prodaja