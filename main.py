from kategorija import unos_kategorije, ispis_svih_kategorija
from korisnik import unos_korisnika, ispis_svih_korisnika
from prodaja import unos_prodaje, ispis_svih_prodaja
from utillities import unos_intervala

korisnici = []
kategorije = []
prodaje = []

running = True
while running:
    print('-'*20)
    print('1. Unos novog korisnika')
    print('2. Unos nove kategorije')
    print('3. Unos nove prodaje')
    print('4. Ispis korisnika')
    print('5. Ispis kategorija')
    print('6. Ispis prodaja')
    print('7. Zaustavi program')
    print('-'*20)

    akcija = unos_intervala(1,7)

    if akcija == 1:
        korisnici.append(unos_korisnika(len(korisnici)+1))
    elif akcija == 2:
        kategorije.append(unos_kategorije(len(kategorije)+1))
    elif akcija == 3:
        prodaje.append(unos_prodaje(korisnici, kategorije, len(prodaje)+1))
    elif akcija == 4:
        ispis_svih_korisnika(korisnici)
    elif akcija == 5:
        ispis_svih_kategorija(kategorije)
    elif akcija == 6:
        ispis_svih_prodaja(prodaje)
    elif akcija == 7:
        running = False

