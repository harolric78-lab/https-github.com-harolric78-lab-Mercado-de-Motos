"""
Genera CSV con comparación de precios de los 30 anuncios más recientes
"""

import csv
from pathlib import Path

DATA = [
    ("Combustión", "Yamaha", "YBR 125", 8500, 2019),
    ("Eléctrica", "Eco", "E-Bike City", 3200, 2023),
    ("Patinete", "Xiaomi", "Mi Pro 2", 2800, 2022),
    ("Combustión", "Honda", "XR 150", 12000, 2020),
    ("Eléctrica", "Eco", "E-Bike Sport", 4500, 2023),
    ("Patinete", "Segway", "Ninebot ES2", 3500, 2021),
    ("Combustión", "Suzuki", "GN 125", 7800, 2018),
    ("Eléctrica", "Volt", "V1 City", 2900, 2023),
    ("Patinete", "Xiaomi", "Mi Essential", 2200, 2022),
    ("Combustión", "Italika", "RT 125", 5500, 2021),
    ("Eléctrica", "Eco", "E-Bike Mountain", 5200, 2023),
    ("Patinete", "Ninebot", "ES1", 2500, 2021),
    ("Combustión", "Yamaha", "FZ 25", 18000, 2022),
    ("Eléctrica", "Volt", "V2 Pro", 6000, 2023),
    ("Patinete", "Xiaomi", "Mi 3", 3000, 2022),
    ("Combustión", "Honda", "CBR 150", 14500, 2021),
    ("Eléctrica", "Eco", "E-Bike Fold", 3800, 2023),
    ("Patinete", "Segway", "Max G30", 4200, 2022),
    ("Combustión", "Kawasaki", "Ninja 300", 25000, 2020),
    ("Eléctrica", "Volt", "V1 Sport", 3400, 2023),
    ("Patinete", "Ninebot", "E22", 3200, 2021),
    ("Combustión", "Bajaj", "Pulsar 150", 9500, 2019),
    ("Eléctrica", "Eco", "E-Bike Cruiser", 4800, 2023),
    ("Patinete", "Xiaomi", "Mi Pro 3", 3600, 2022),
    ("Combustión", "Royal Enfield", "Classic 350", 22000, 2021),
    ("Eléctrica", "Volt", "V2 City", 5500, 2023),
    ("Patinete", "Segway", "F25", 2800, 2021),
    ("Combustión", "Yamaha", "R15", 16000, 2022),
    ("Eléctrica", "Eco", "E-Bike Urban", 3100, 2023),
    ("Patinete", "Ninebot", "ES4", 4000, 2022),
]

def save_comparison_csv(path: str = "data/comparacion_precios.csv") -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["tipo", "marca", "modelo", "precio_cup", "anio"])
        writer.writerows(DATA)
    print(f"[OK] CSV guardado en {path}")


def print_summary() -> None:
    tipos = {}
    for tipo, _, _, precio, _ in DATA:
        tipos.setdefault(tipo, []).append(precio)

    print("\nPromedios por tipo:")
    for tipo, precios in sorted(tipos.items()):
        promedio = sum(precios) / len(precios)
        print(f"  {tipo}: {promedio:,.0f} CUP")


if __name__ == "__main__":
    save_comparison_csv()
    print_summary()
