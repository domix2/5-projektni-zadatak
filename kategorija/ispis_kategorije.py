from artikl import ispis_artikla
def get_kategorija(redni_broj, kategorija):
    return f"{redni_broj}. {kategorija}"

def ispis_svih_kategorija(kategorije):
    print('Ispis svih kategorija:')
    for kategorija in kategorije:
        print(f"{kategorija['naziv']}:")
        for kategorija['artikl'] in kategorija['artikli']:
            ispis_artikla(kategorija['artikl'])
