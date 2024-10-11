
#Project
from .Auto import Auto


class Teherauto(Auto):
    def __init__(self, rendszam, marka, berleti_dij, max_terheles):
        super().__init__(rendszam, marka, berleti_dij)
        self.max_terheles = max_terheles

    def __str__(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.marka.name}, Bérleti díj: {self.berleti_dij}, Max terhelés: {self.max_terheles}"
