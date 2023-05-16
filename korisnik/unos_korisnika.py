from utillities import unos_telefona,unos_mail_m
from .korisnik import Korisnik

def unos_korisnika(redni_broj):
    ime = input(f'Unesite ime {redni_broj}. korisnika:').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. korisnika:').capitalize()
    email = unos_mail_m(f'Unesite email {redni_broj}. korisnika: ').strip()
    telefon = unos_telefona(f'Unesite telefon {redni_broj}. korisnika:')
    return Korisnik(ime, prezime, telefon,email)
