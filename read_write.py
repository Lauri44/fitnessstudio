import csv
import os
from global_stuff import Kategorie, Kunde

#################| Import Code Section |################


def __on_import() -> None:
    """This function contains all checks to ensuere the moduel can run properly"""
    if not os.path.exists("./kunden.csv"):
        with open("./kunden.csv", "x") as file:
            _ = file.write("id_kunde,name,vorname,kategorie,groesse,gewicht,PIN")


__on_import()


#######################################################


def saveKunden(kunden_daten: list[Kunde], new: bool = False) -> None:
    """
Saves customer data in a csv file.\n
Dict is required to ensure that all values are in the correct order 
    """

    mode: str = "w"

    if new:
        mode = "a"
 
    with open("kunden.csv", mode) as file:
        csv.DictWriter(file, fieldnames=kunden_daten[0].keys()).writerows(kunden_daten)


def getKunden() -> list[Kunde]:
    """Returns a list of dictionaries with the correct datatypes for all vaules"""
    with open("kunden.csv", "r") as file:
        kunden: list[Kunde] = []
        
        
        for kunde in csv.DictReader(file):
            print(kunde)
            kunden.append(
                {
                    "id_kunde": kunde["id_kunde"],
                    "name": kunde["name"],
                    "vorname": kunde["vorname"],
                    "kategorie": Kategorie(kunde["kategorie"]),
                    "groesse": float(kunde["groesse"]),
                    "gewicht": float(kunde["gewicht"]),
                    "PIN": kunde["PIN"],
                    "locked": bool(kunde["locked"]),
                }
            )

    return kunden

