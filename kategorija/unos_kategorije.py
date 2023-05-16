from artikl import unos_artikla
from utillities import unos_pozitivnog_cijelog_broja
from .kategorija import Kategorija
def unos_kategorije(redni_broj):
    naziv = input(f'Unesite naziv {redni_broj}. kategorije:').capitalize()
    artikli = []
    broj_artikala = unos_pozitivnog_cijelog_broja(f'Unesite broj artikala za {redni_broj}. kategoriju:')
    for i in range(1, broj_artikala + 1):
        artikl = unos_artikla(i)
        artikli.append(artikl)
    return Kategorija(naziv, artikli)

