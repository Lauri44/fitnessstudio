#Projekt Fitnesstudio
#Ein Kollege
#18.11.2021
#Zusammenstellung verschiedener Funktionen der Applikation Fitnesstudio
from funktionen import neuer_kunde, anmeldung, berechne_bmi, auswertung_bmi
from global_stuff import Kunde



def user_menu():

    print("""

<------------| USER OPTIONS |------------> 

            1. PIN ändern
            2. BMI berechenen
            3. Beenden

""")

    while True:
        user_input = input("$ What do you wanna do?(1 2 or 3): ")

        match user_input:
            case '1':
                ...
            case '2':
                bmi: float = berechne_bmi(current_user['groesse'], current_user['gewicht'])


def main():
    """Startfunktion für den Aufruf verschiedener Funktionen der Applikation Fitnessstudio"""
    global current_user
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

                if not bool(current_user):
                    continue

                user_menu()

            case '3':
                print("Good bye! Have a beautiful day :D")
                return

            case _:
                print("Das ist keine Option!")
                continue


    



if __name__ == "__main__":
    main()


