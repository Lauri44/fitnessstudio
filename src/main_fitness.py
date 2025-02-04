#Projekt Fitnesstudio
#Alexander und Laurentius
#18.11.2021
#Zusammenstellung verschiedener Funktionen der Applikation Fitnesstudio
from funktionen import neuer_kunde, anmeldung, berechne_bmi, auswertung_bmi, change_pin
from global_stuff import Kunde






def user_menu(current_user: Kunde) -> None:

    print("""

<------------| USER OPTIONS |------------> 

            1. PIN ändern
            2. BMI berechenen
            3. Beenden

""")

    while True:
        user_input: str = input("$ What do you wanna do?(1 2 or 3): ")

        match user_input:
            case '1':
                change_pin(current_user)
            case '2':
                bmi: float = berechne_bmi(current_user['groesse'], current_user['gewicht'])
                auswertung_bmi(bmi, current_user['id_kunde'])
            case '3':
                print("\nGood Bye! Have beatiful day :D\n")
                return
            case _:
                print("\nDiese Option existiert nicht\n")



def main() -> None:
    """Startfunktion für den Aufruf verschiedener Funktionen der Applikation Fitnessstudio"""
    current_user: Kunde
    # TODO: ASCII rüber kopieren

    print("""

<==============| OPTIONS |==============>

            1. Registrieren
            2. Anmelden
            3. Beenden

""")
    
    while True:
        user_input = input("$ What do you wanna do?(1, 2 or 3): ")

        match user_input:
            case '1':
                neuer_kunde()

            case '2':
                current_user = anmeldung()

                if current_user["id_kunde"] == "":
                    continue

                if not user_menu(current_user):
                    return

            case '3':
                print("\nGood bye! Have a beautiful day :D\n")
                return

            case _:
                print("\nDas ist keine Option!\n")
                continue
    

if __name__ == "__main__":
    main()
