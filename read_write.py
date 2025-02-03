import csv
import os
from global_stuff import Kategorie, Kunde

#################| Import Code Section |################


def __on_import() -> None:
    """This function contains all checks to ensuere the moduel can run properly"""
    if not os.path.exists("./kunden.csv"):
        with open("./kunden.csv", "x") as file:
            _ = file.write("id_kunde;name;vorname;kategorie;groesse;gewicht;PIN")


__on_import()


#######################################################


def saveKunde(kunden_daten: Kunde) -> None:
    """
Saves customer data in a csv file.\n
Dict is required to ensure that all values are in the correct order 
    """
    with open("kunden.csv", "w") as file:
        csv.DictWriter(file, fieldnames=kunden_daten.keys()).writerow(kunden_daten)


def getKunden() -> list[Kunde]:
    """Returns a list of dictionaries with the correct datatypes for all vaules"""
    with open("kunden.csv", "r") as file:
        kunden: list[Kunde] = []

        for kunde in csv.reader(file):
            kunden.append(
                {
                    "id_kunde": kunde[0],
                    "name": kunde[1],
                    "vorname": kunde[2],
                    "kategorie": Kategorie(kunde[3]),
                    "groesse": float(kunde[4]),
                    "gewicht": float(kunde[5]),
                    "PIN": kunde[6],
                    "locked": bool(kunde[7]),
                }
            )

    return kunden
