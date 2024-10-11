#External
from datetime import date


#Project
from .Auto import AutoMarka
from .Berles import Berles
from .Szemelyauto import Szemelyauto
from .Teherauto import Teherauto


class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaad(self, auto):
        self.autok.append(auto)

    def auto_berles(self, rendszam, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                if not any(berles.auto.rendszam == rendszam and berles.datum == datum for berles in self.berlesek):
                    self.berlesek.append(Berles(auto, datum))
                    return auto.berleti_dij
        return None

    def berles_leomondasa(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                return True
        return False

    def autok_listazasa(self):
        return self.autok if self.autok else "Nincs autó."

    def berlesek_listazasa(self):
        return self.berlesek if self.berlesek else "Nincs aktív bérlés."


# Példa adatok
def adat_betoltes():
    kolcsonzo = Autokolcsonzo("Kolcsonzo_KFT")
    autok = [
        Szemelyauto("ABC-123", AutoMarka.HONDA, 10000, 5),
        Teherauto("XYZ-789", AutoMarka.FORD, 15000, 1000),
        Szemelyauto("DEF-456", AutoMarka.TOYOTA, 12000, 5),
        Teherauto("UVW-345", AutoMarka.MERCEDES, 18000, 800),
        Szemelyauto("GHI-789", AutoMarka.BMW, 13000, 5),
        Teherauto("RST-111", AutoMarka.VOLVO, 20000, 1200),
        Szemelyauto("JKL-101", AutoMarka.AUDI, 14000, 5),
        Teherauto("OPQ-222", AutoMarka.RENAULT, 16000, 900),
        Szemelyauto("MNO-303", AutoMarka.SKODA, 11000, 5),
        Teherauto("HIJ-345", AutoMarka.MAN, 19000, 1300),
        Szemelyauto("PQR-456", AutoMarka.OPEL, 11500, 5),
        Teherauto("LMN-567", AutoMarka.IVECO, 17500, 700),
        Szemelyauto("STU-678", AutoMarka.CITROEN, 12500, 5),
        Teherauto("GHI-769", AutoMarka.SCANIA, 18500, 900),
        Szemelyauto("VWX-999", AutoMarka.SEAT, 13500, 5)
    ]

    for auto in autok:
        kolcsonzo.auto_hozzaad(auto)


    kolcsonzo.auto_berles("DEF-456", date(2024, 11, 5))
    kolcsonzo.auto_berles("UVW-345", date(2024, 11, 7))
    kolcsonzo.auto_berles("GHI-789", date(2024, 11, 10))
    kolcsonzo.auto_berles("JKL-101", date(2024, 11, 12))
    kolcsonzo.auto_berles("ABC-123", date(2024, 11, 1))
    kolcsonzo.auto_berles("XYZ-789", date(2024, 11, 3))
    return kolcsonzo
