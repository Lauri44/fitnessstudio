import random
from read_write import getKunden, saveKunde
from global_stuff import Kategorie, Kunde

def anmeldung() -> Kunde:
    """Anmeldung des users\n
Wenn anmeldung fehl schlägt sind werte von Kunde leer
    """
    kunden = getKunden()

    id_kunde = input("Bitte geben Sie ihre ID an: ")

    current_customer: Kunde = {
        "id_kunde": "",
        "name": "",
        "vorname": "",
        "kategorie": Kategorie.S,
        "groesse": 0.0,
        "gewicht": 0.0,
        "PIN": "",
        "locked": True,
    }

    exists: bool = False
    for kunde in kunden:
        if id_kunde == kunde["id_kunde"]:
            current_customer = kunde
            exists = True

    if not exists:
        print("Diese ID existiert nicht!")
        return current_customer

    if current_customer["locked"]:
        print("Ihr account ist gesperrt!!!\nBitte kontaktieren Side den Kudenservice!")
        return current_customer

    for foo in range(4):
        if foo >= 3:
            current_customer["locked"] = True
            print("Zu viele Fehlversuche!\n\nIhr account wurde gesperrt!!!\nBitte kontaktieren Side den Kudenservice!")
            return current_customer

        pin: str = input("Bitte geben Sie ihren PIN ein: ")

        if pin != current_customer["PIN"]:
            continue
        else:
            break

    print("Sie wurden erfolgreich angemeldet :D")

    return current_customer


def neuer_kunde() -> None:
    """liest die Daten eines Kunden ein und erzeugt mit Hilfe von Zufallszahlen eine KundenID. Die Daten des Kunden
    werden als Tupel zurückgegeben """
    print("Bitte geben Sie ihre Daten ein: ")
    name = input('Name: ')
    vorname = input('Vorname: ')

    kategorie = input('Kategorie: ') # TODO: Input check fehlt!!!!!
    
    while True:
        try: 
            groesse =  float(input('Größe in m: '))
            gewicht = float(input('Gewicht in kg: '))
        except:
            print("Bitte geben Sie nur Zahlen ein")
            continue
        break

    random.seed()
    id_kunde = random.randint(1000, 10000)
    
    saveKunde({
        "id_kunde": str(id_kunde),
        "name": name,
        "vorname": vorname,
        "kategorie": Kategorie.S,
        "groesse": groesse,
        "gewicht": gewicht,
        "PIN": '0000',
        "locked": False,
    })


def berechne_bmi(groesse: float, gewicht: float) -> float:
    """ berechnet den Body-Mass-Index anhand der klassischen Formel
    :param groesse: float
    :param gewicht: float
    """
    return gewicht/groesse ** 2


def auswertung_bmi(bmi: float, id_kunde: int) -> None:
    """wertet den Body-Mass-Index für einen über die KundenID referenzierten Kunden gemäß der Kategorien
    Unter-, Normal- und Übergewicht aus
    :parameter id_kunde: str
    :param bmi: float    """
    if bmi > 25:
        print('Der Kunde mit der ID {0:6} hat mit einem BMI von {1:5.2f} Übergewicht'.format(id_kunde, bmi))
    elif bmi < 20:
        print('Der Kunde mit der ID {0:6} hat mit einem BMI von {1:5.2f} Untergewicht'.format(id_kunde, bmi))
    print('Der Kunde mit der ID {0:6} hat mit einem BMI von {1:5.2f} Normalgewicht'.format(id_kunde, bmi))
