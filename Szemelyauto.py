
#Project
from Auto import Auto


class Szemelyauto(Auto):
    def __init__(self, rendszam, marka, berleti_dij, utas_szam):
        super().__init__(rendszam, marka, berleti_dij)
        self.utas_szam = utas_szam

    def __str__(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.marka.name}, Bérleti díj: {self.berleti_dij}, Utasok száma: {self.utas_szam}"
