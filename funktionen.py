import random
from read_write import getKunden, saveKunden
from global_stuff import Kategorie, Kunde
import re

def anmeldung() -> Kunde:
    """Anmeldung des users\n
Wenn Anmeldung fehl schlägt sind werte von Kunde leer
    """
    kunden: list[Kunde] = getKunden()
    

    id_kunde = input("Bitte geben Sie ihre ID an: ")

    empty_kunde: Kunde = {
        "id_kunde": "",
        "name": "",
        "vorname": "",
        "kategorie": Kategorie.S,
        "groesse": 0.0,
        "gewicht": 0.0,
        "PIN": "",
        "locked": True,
    }


    current_customer: Kunde = empty_kunde #Kein plan wie ich das anderas handhaben soll wenn Kunden werte required bleiben sollen
    exists: bool = False
    for kunde in kunden:
        if id_kunde == kunde["id_kunde"]:
            current_customer = kunde
            exists = True

    if not exists:
        print("Diese ID existiert nicht!")
        return empty_kunde

    if current_customer["locked"]:
        print("Ihr account ist gesperrt!!!\nBitte kontaktieren Side den Kudenservice!")
        return empty_kunde
    
    index: int = kunden.index(current_customer)

    for foo in range(4):
        if foo >= 3:
            kunden[index]["locked"] = True
            print("Zu viele Fehlversuche!\n\nIhr account wurde gesperrt!!!\nBitte kontaktieren Side den Kudenservice!")
            
            return empty_kunde

        pin: str = input("Bitte geben Sie ihren PIN ein: ")

        if pin != current_customer["PIN"]:
            continue
        else:
            break
    print("(Mit q können sie jeder zeit abbrechen)")

    print("Sie wurden erfolgreich angemeldet :D")

    return current_customer

def change_pin(kunde: Kunde):
    """Ändert den PIN eines Kunden speichert den neuen PIN ab"""
    current_pin: str = input("$ Geben Sie den aktuelle PIN an: ")

    kunden: list[Kunde] = getKunden()
    
    if current_pin == kunde["PIN"]:
        while True:
            new_pin: str = input("$ Bitte geben sie den neuen PIN an: ")
            if new_pin == kunde["PIN"]:
                print("Dieser PIN existiert bereits!\nBitte geben Sei einen anderen ein!")
                continue
            elif len(new_pin) != 4:
                print("Der PIN muss genua vier Zeichen lang sein!")
                continue
            
            kunden[kunden.index(kunde)]["PIN"] = new_pin
            break
        saveKunden(kunden)
    else:
        print("Das wahr der Falsche PIN!")
        
    return


def neuer_kunde() -> None:
    """liest die Daten eines Kunden ein und erzeugt mit Hilfe von Zufallszahlen eine KundenID. Die Daten des Kunden
    werden als Tupel zurückgegeben """
    print("Bitte geben Sie ihre Daten ein: ")
    name = input('Name: ')
    vorname = input('Vorname: ')

    print("""

<<<<<<<<<<<<<| CATEGORIES |>>>>>>>>>>>>>
            
            S = Stammkunde
            N = Neukunde
            P = Probeabo
            K = Krankenkasse

    """)

    while True:
        kategorie = input('Kategorie: ').upper()
         
        if re.match(r"^[S|N|P|K]$", kategorie):
            kategorie = Kategorie(kategorie)
            break

        print("Kategorie existiert nicht!\n")
        
    
    while True:
        try: 
            groesse =  float(input('Größe in m: '))
            gewicht = float(input('Gewicht in kg: '))
        except:
            print("Bitte geben Sie nur Zahlen ein")
            continue
        break

    random.seed()
    id_kunde: str = str(random.randint(1000, 10000))
    
    saveKunden([{
        "id_kunde": id_kunde,
        "name": name,
        "vorname": vorname,
        "kategorie": kategorie,
        "groesse": groesse,
        "gewicht": gewicht,
        "PIN": '0000',
        "locked": False,
    }], True)


def berechne_bmi(groesse: float, gewicht: float) -> float:
    """ berechnet den Body-Mass-Index anhand der klassischen Formel
    :param groesse: float
    :param gewicht: float
    """
    return gewicht/groesse ** 2


def auswertung_bmi(bmi: float, id_kunde: str) -> None:
    """wertet den Body-Mass-Index für einen über die KundenID referenzierten Kunden gemäß der Kategorien
    Unter-, Normal- und Übergewicht aus
    :parameter id_kunde: str
    :param bmi: float    """
    if bmi > 25:
        print('Der Kunde mit der ID {0:6} hat mit einem BMI von {1:5.2f} Übergewicht'.format(id_kunde, bmi))
    elif bmi < 20:
        print('Der Kunde mit der ID {0:6} hat mit einem BMI von {1:5.2f} Untergewicht'.format(id_kunde, bmi))
    print('Der Kunde mit der ID {0:6} hat mit einem BMI von {1:5.2f} Normalgewicht'.format(id_kunde, bmi))
