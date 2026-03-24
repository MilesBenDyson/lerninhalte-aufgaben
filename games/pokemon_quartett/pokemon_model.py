# klasse pokemonkarten
class Pokemon:
    def __init__(self, name, level, kp, angr, vert, spez_ang, spez_vert):
        self.name = name
        self.level = self._check(level)
        self.kraftpunkte = self._check(kp)
        self.angriff = self._check(angr)
        self.verteidigung = self._check(vert)
        self.spezialangriff = self._check(spez_ang)
        self.spezialverteidigung = self._check(spez_vert)
    def __str__(self):
        return (f"{self.name}\n\n{'Level:':<20} {self.level}\n{'Kraftpunkte:':<20} {self.kraftpunkte}\n{'Angriff:':<20} {self.angriff}\n{'Verteidigung:':<20} {self.verteidigung}\n{'Spez.Angriff:':<20} {self.spezialangriff}\n{'Spez.Verteidigung:':<20} {self.spezialverteidigung}\n\n")

    # einen wertecheck
    def _check(self, wert):
        try:
            wert = int(wert)
        except (ValueError, TypeError):
            print(f"{wert} ist kein gültiger Wert. Der Wert wird auf 1 gesetzt.")
            wert = 1
        if wert > 100:
            return 100
        if wert < 0:
            return 1
        return wert