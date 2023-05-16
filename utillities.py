from datetime import date
def unos_pozitivnog_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception('Morate ponovno upisati cijeli pozitivni broj')
        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj

def unos_realnog_pozitivnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate ponovno upisati realni broj!')

        except ValueError:
            print('Unesli ste znak a ne realni broj.')
        except Exception as e:
            print(e)
        else:
            return broj

def unos_datuma(poruka):
    while True:
        try:
            dan = int(input(poruka))
            mjesec = int(input(f'Unesite mjesec isteka prodaje:'))
            godina = int(input(f'Unesite godinu isteka prodaje:'))
            datum = date(godina, mjesec, dan)
        except ValueError as e:
            print(e)
        else:
            return datum

def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u intervalu {min} - {max}:"))

            if broj<min or broj>max:
                raise Exception(f"Unesite broj unutar intervala {min} - {max}.")

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj

def unos_telefona(poruka):
    while True:
        try:
            broj = str(unos_pozitivnog_cijelog_broja(poruka))

            if len(broj) !=8:
                raise Exception(f"Broj telefona mora imati 8 znamenaka!")

        except Exception as e:
            print(e)
        else:
            return broj
def unos_mail_m(poruka):
    while True:
        try:
            email = input(poruka)
            index = email.index('@')

        except ValueError:
            print('Uneseni mail mora sadržavati znak @!')

        else:
            return email