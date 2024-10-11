#External
from datetime import date
import sys

#Project
from .Autokolcsonzo import Autokolcsonzo
from .Valasztas import Valasztas
from .Errorhandler import catch_all_exceptions

class AppHandler:
    def __init__(self):
        pass

    @catch_all_exceptions
    def print_menu(self):

        print("\n--- Autókölcsönző Rendszer ---")
        for valasztas in Valasztas:
            print(valasztas.value)

    @catch_all_exceptions
    def convert_menu_input(self, data: str):

        match data:
            case '1':
                data = Valasztas.BERLES
            case '2':
                data = Valasztas.LEMONDAS
            case '3':
                data = Valasztas.LISTAZAS_BERLES
            case '4':
                data = Valasztas.LISTAZAS_AUTO
            case '0':
                data = Valasztas.KILEPES
        return data

    @catch_all_exceptions
    def get_data_from_input(self):

        rendszam = input("Adja meg az autó rendszámát: ")
        ev = int(input("Adja meg a bérlés évét: "))
        honap = int(input("Adja meg a bérlés hónapját: "))
        nap = int(input("Adja meg a bérlés napját: "))
        datum = date(ev, honap, nap)
        return rendszam, datum

    @catch_all_exceptions
    def berles(self, kolcsonzo: Autokolcsonzo):

        rendszam, datum = self.get_data_from_input()
        ar = kolcsonzo.auto_berles(rendszam, datum)
        if ar:
            print(f"Bérlés sikeres! Ár: {ar} Ft")
        else:
            print("A megadott autó nem elérhető a kiválasztott dátumon.")

    @catch_all_exceptions
    def lemondas(self, kolcsonzo: Autokolcsonzo):

        rendszam, datum = self.get_data_from_input()
        siker = kolcsonzo.berles_leomondasa(rendszam, datum)
        if siker:
            print("Bérlés lemondása sikeres!")
        else:
            print("Nincs ilyen bérlés.")

    @catch_all_exceptions
    def listazas(self, kolcsonzo: Autokolcsonzo, auto: bool = False):

        if auto:
            autok = kolcsonzo.autok_listazasa()
            if autok == 'Nincs autó':
                print(autok)
            else:
                for auto in autok:
                    print(auto)
        else:
            berlesek = kolcsonzo.berlesek_listazasa()
            if berlesek == "Nincs aktív bérlés.":
                print(berlesek)
            else:
                for berles in berlesek:
                    print(berles)

    def kilepes(self):
        print("Kilépés a programból.")
        sys.exit()

