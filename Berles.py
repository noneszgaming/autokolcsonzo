class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"Bérlés - Autó: {self.auto.rendszam}, Dátum: {self.datum}"
