

#Project
from .Autokolcsonzo import adat_betoltes
from .Apphandler import AppHandler
from .Valasztas import Valasztas




def main():
    app = AppHandler()
    kolcsonzo = adat_betoltes()

    while True:
        app.print_menu()
        valasztas = input("Választás: ")
        valasztas = app.convert_menu_input(valasztas)

        match valasztas:
            case Valasztas.BERLES:
                app.berles(kolcsonzo)
            case Valasztas.LEMONDAS:
                app.lemondas(kolcsonzo)
            case Valasztas.LISTAZAS_BERLES:
                app.listazas(kolcsonzo)
            case Valasztas.LISTAZAS_AUTO:
                app.listazas(kolcsonzo, True)
            case Valasztas.KILEPES:
                app.kilepes()
            case _:
                print("Érvénytelen választás. Próbálja újra!")


if __name__ == "__main__":
    main()
