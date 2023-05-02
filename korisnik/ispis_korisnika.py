
def ispis_korisnika(korisnik):
    print('Informacije o korisniku:')
    print(f"\tIme: {korisnik['ime']}")
    print(f"\tPrezime: {korisnik['prezime']}")
    print(f"\tTelefon: {korisnik['telefon']}")
    print(f"\tEmail: {korisnik['email']}")

def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik['ime']} {korisnik['prezime']}"

def ispis_svih_korisnika(korisnici):
    print('Ispis svih korisnika:')
    for korisnik in korisnici:
        ispis_korisnika(korisnik)