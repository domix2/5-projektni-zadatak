from artikl import unos_artikla
from utillities import unos_pozitivnog_cijelog_broja
def unos_kategorije(redni_broj):
    kategorija = {}
    naziv = input(f'Unesite naziv {redni_broj}. kategorije:').capitalize()
    kategorija['naziv'] = naziv
    kategorija['artikli'] = []
    broj_artikala = unos_pozitivnog_cijelog_broja(f'Unesite broj artikala za {redni_broj}. kategoriju:')
    for i in range(1, broj_artikala + 1):
        artikl = unos_artikla(i)
        kategorija['artikli'].append(artikl)
    return kategorija

