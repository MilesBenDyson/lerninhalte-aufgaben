"""🥒 Aufgabe: JSON-Frühstücksliste

Du hast eine kleine Einkaufsliste fürs verkatert-taugliche Frühstück. Speichere sie in einer JSON-Datei und lade sie später wieder."""
import json

einkaufsliste = {"Brötchen": 4, "Rollmops": 2, "Multivitaminsaft": 1, "Kopfschmerztablette": 1, "Banane": 2}

with open("fruehstueck.json", "w", encoding="utf-8") as f:
    json.dump(einkaufsliste, f, ensure_ascii=False, indent=2)

with open("fruehstueck.json", "r", encoding="utf-8") as f:
    file = json.load(f)

print(file)