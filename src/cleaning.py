"""
Limpieza y normalización de datos de motos
"""

import pandas as pd
import re
from pathlib import Path


def load_raw(path: str = "data/raw/motos_raw.csv") -> pd.DataFrame:
    """Carga los datos crudos."""
    df = pd.read_csv(path)
    print(f"[INFO] Cargados {len(df)} registros desde {path}")
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina anuncios duplicados por URL o título+precio."""
    before = len(df)
    df = df.drop_duplicates(subset=["url"], keep="first")
    df = df.drop_duplicates(subset=["titulo", "precio"], keep="first")
    print(f"[LIMPIEZA] Duplicados eliminados: {before - len(df)}")
    return df


def clean_prices(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y normaliza la columna de precios."""
    df = df.copy()
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce")

    # Eliminar precios absurdos (menos de 1000 CUP o más de 100M)
    df = df[(df["precio"] >= 1000) & (df["precio"] <= 100_000_000)]

    # Crear columna de precio en miles para análisis
    df["precio_miles"] = (df["precio"] / 1000).round(1)

    print(f"[LIMPIEZA] Precios válidos: {df['precio'].notna().sum()}")
    return df


def normalize_brands(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza nombres de marcas."""
    df = df.copy()

    correcciones = {
        "suzuky": "Suzuki",
        "yamaha": "Yamaha",
        "honda": "Honda",
        "kawasaki": "Kawasaki",
        "italika": "Italika",
        "bajaj": "Bajaj",
    }

    df["marca"] = df["marca"].replace(correcciones)
    df["marca"] = df["marca"].str.strip().str.title()

    # Reemplazar "Desconocida" por NaN para análisis
    df.loc[df["marca"] == "Desconocida", "marca"] = None

    print(f"[LIMPIEZA] Marcas únicas: {df['marca'].nunique()}")
    return df


def clean_locations(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza ubicaciones."""
    df = df.copy()
    df["ubicacion"] = df["ubicacion"].str.strip().str.title()
    df["ubicacion"] = df["ubicacion"].fillna("No especificada")
    return df


def extract_year(text: str) -> int | None:
    """Intenta extraer el año del título."""
    if not isinstance(text, str):
        return None
    match = re.search(r"\b(19[89]\d|20[0-2]\d)\b", text)
    return int(match.group(1)) if match else None


def add_year_column(df: pd.DataFrame) -> pd.DataFrame:
    """Añade columna de año extraída del título."""
    df = df.copy()
    df["anio"] = df["titulo"].apply(extract_year)
    print(f"[LIMPIEZA] Años detectados: {df['anio'].notna().sum()}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Pipeline completo de limpieza."""
    print("\n" + "=" * 50)
    print("  LIMPIEZA DE DATOS")
    print("=" * 50)

    df = remove_duplicates(df)
    df = clean_prices(df)
    df = normalize_brands(df)
    df = clean_locations(df)
    df = add_year_column(df)

    # Eliminar filas sin precio (dato clave)
    df = df.dropna(subset=["precio"])

    # Reset index
    df = df.reset_index(drop=True)

    print(f"\n[RESULTADO] Registros finales: {len(df)}")
    return df


def save_clean(df: pd.DataFrame, path: str = "data/processed/motos_clean.csv") -> None:
    """Guarda datos limpios."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8")
    print(f"[OK] Datos limpios guardados en {path}")


if __name__ == "__main__":
    df_raw = load_raw()
    df_clean = clean_data(df_raw)
    save_clean(df_clean)
