"""
Pipeline principal: Scraping → Limpieza → Análisis
"""

from scraping.scraper import scrape_revolico, save_to_csv
from src.cleaning import load_raw, clean_data, save_clean
from src.analysis import load_clean, run_analysis


def main():
    print("=" * 50)
    print("  PROYECTO: MOTOS EN CUBA")
    print("  Ciencia de Datos - Revolico")
    print("=" * 50)

    # FASE 1: Scraping
    print("\n📡 FASE 1: Extracción de datos")
    datos = scrape_revolico(max_pages=10)
    save_to_csv(datos)

    # FASE 2: Limpieza
    print("\n🧹 FASE 2: Limpieza de datos")
    df_raw = load_raw()
    df_clean = clean_data(df_raw)
    save_clean(df_clean)

    # FASE 3: Análisis
    print("\n📊 FASE 3: Análisis y visualización")
    df = load_clean()
    run_analysis(df)

    print("\n" + "=" * 50)
    print("  ¡PROYECTO COMPLETADO!")
    print("=" * 50)


if __name__ == "__main__":
    main()
