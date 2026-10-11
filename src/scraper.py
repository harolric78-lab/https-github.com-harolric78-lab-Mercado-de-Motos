"""
Scraping de anuncios de motos en Revolico (Cuba)
Extrae: título, precio, marca, modelo, año, ubicación y fecha
"""

import csv
import time
import random
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = "https://www.revolico.com"
MOTOS_URL = f"{BASE_URL}/anuncios-en-cuba/motos"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_page(url: str) -> str:
    """Descarga el HTML de una página."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"[ERROR] {e}")
        return ""


def parse_price(text: str) -> float | None:
    """Extrae el precio en CUP de un texto."""
    if not text:
        return None
    numbers = re.findall(r"[\d,]+", text.replace(",", ""))
    return float(numbers[0]) if numbers else None


def parse_title(title: str) -> dict:
    """Intenta extraer marca y modelo del título."""
    marcas = [
        "Yamaha", "Honda", "Suzuki", "Kawasaki", "BMW", "KTM",
        "Italika", "Royal Enfield", "Bajaj", "TVS", "Hero",
        "Jawa", "Ducati", "Harley-Davidson", "Suzuky", "Monster"
    ]
    marca = "Desconocida"
    for m in marcas:
        if m.lower() in title.lower():
            marca = m
            break

    modelo = title.replace(marca, "").strip(" -") if marca != "Desconocida" else ""
    return {"marca": marca, "modelo": modelo}


def extract_ads_from_page(html: str) -> list[dict]:
    """Extrae anuncios individuales de una página de listado."""
    soup = BeautifulSoup(html, "lxml")
    ads = []

    items = soup.select("article, .listing-item, .ad-item")
    if not items:
        items = soup.select("div[class*='item'], li[class*='ad']")

    for item in items:
        title_el = item.select_one("h2 a, .title a, a[class*='title']")
        price_el = item.select_one(".price, [class*='price']")
        loc_el = item.select_one(".location, [class*='location']")
        date_el = item.select_one(".date, [class*='date']")

        if not title_el:
            continue

        title = title_el.get_text(strip=True)
        link = title_el.get("href", "")
        if link and not link.startswith("http"):
            link = BASE_URL + link

        info = parse_title(title)

        ads.append({
            "titulo": title,
            "precio": parse_price(price_el.get_text(strip=True) if price_el else ""),
            "marca": info["marca"],
            "modelo": info["modelo"],
            "ubicacion": loc_el.get_text(strip=True) if loc_el else "",
            "fecha": date_el.get_text(strip=True) if date_el else "",
            "url": link
        })

    return ads


def scrape_revolico(max_pages: int = 10) -> list[dict]:
    """Scrapea múltiples páginas de Revolico."""
    all_ads = []

    for page in range(1, max_pages + 1):
        url = f"{MOTOS_URL}?page={page}" if page > 1 else MOTOS_URL
        print(f"[INFO] Scraping página {page}: {url}")

        html = get_page(url)
        if not html:
            continue

        ads = extract_ads_from_page(html)
        if not ads:
            print("[INFO] No se encontraron más anuncios. Fin.")
            break

        all_ads.extend(ads)
        print(f"[INFO] {len(ads)} anuncios en página {page}. Total: {len(all_ads)}")

        time.sleep(random.uniform(2, 4))

    return all_ads


def save_to_csv(data: list[dict], path: str = "data/raw/motos_raw.csv") -> None:
    """Guarda los datos en un archivo CSV."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    if not data:
        print("[WARN] No hay datos para guardar.")
        return

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"[OK] Datos guardados en {path}")


if __name__ == "__main__":
    print("=" * 50)
    print("  SCRAPER MOTOS REVOLICO")
    print("=" * 50)
    datos = scrape_revolico(max_pages=10)
    save_to_csv(datos)
    print(f"\n✅ Total extraído: {len(datos)} anuncios")
