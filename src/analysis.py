"""
Análisis y visualización de datos de motos en Cuba
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_theme(style="whitegrid")
FIGURES_DIR = Path("outputs/figures")
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def load_clean(path: str = "data/processed/motos_clean.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"[INFO] {len(df)} registros cargados para análisis")
    return df


def basic_stats(df: pd.DataFrame) -> None:
    """Estadísticas descriptivas."""
    print("\n" + "=" * 50)
    print("  ESTADÍSTICAS BÁSICAS")
    print("=" * 50)
    print(f"\nTotal de anuncios: {len(df)}")
    print(f"\nPrecio (CUP):")
    print(f"  Media:       {df['precio'].mean():,.0f}")
    print(f"  Mediana:     {df['precio'].median():,.0f}")
    print(f"  Mínimo:      {df['precio'].min():,.0f}")
    print(f"  Máximo:      {df['precio'].max():,.0f}")
    print(f"  Desviación:  {df['precio'].std():,.0f}")


def plot_price_distribution(df: pd.DataFrame) -> None:
    """Histograma de precios."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df["precio_miles"], bins=30, edgecolor="black", alpha=0.7)
    ax.set_xlabel("Precio (miles CUP)")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Distribución de precios de motos en Cuba")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "precio_distribucion.png", dpi=150)
    plt.close()
    print("[OK] Gráfico: precio_distribucion.png")


def plot_top_brands(df: pd.DataFrame, top: int = 10) -> None:
    """Gráfico de barras: marcas más comunes."""
    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df["marca"].value_counts().head(top)
    counts.plot(kind="bar", ax=ax, color=sns.color_palette("husl", len(counts)))
    ax.set_title(f"Top {top} marcas más publicadas")
    ax.set_xlabel("Marca")
    ax.set_ylabel("Número de anuncios")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "top_marcas.png", dpi=150)
    plt.close()
    print("[OK] Gráfico: top_marcas.png")


def plot_price_by_brand(df: pd.DataFrame, top: int = 8) -> None:
    """Boxplot: precio por marca."""
    marcas_top = df["marca"].value_counts().head(top).index
    df_filtered = df[df["marca"].isin(marcas_top)]

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df_filtered, x="marca", y="precio_miles", ax=ax)
    ax.set_title(f"Precio por marca (top {top})")
    ax.set_xlabel("Marca")
    ax.set_ylabel("Precio (miles CUP)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "precio_por_marca.png", dpi=150)
    plt.close()
    print("[OK] Gráfico: precio_por_marca.png")


def plot_top_models(df: pd.DataFrame, top: int = 15) -> None:
    """Gráfico de barras: modelos más comunes."""
    modelos = df["modelo"].value_counts().head(top)
    if len(modelos) == 0:
        print("[WARN] No hay modelos para graficar")
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    modelos.plot(kind="bar", ax=ax, color=sns.color_palette("viridis", len(modelos)))
    ax.set_title(f"Top {top} modelos más publicados")
    ax.set_xlabel("Modelo")
    ax.set_ylabel("Número de anuncios")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "top_modelos.png", dpi=150)
    plt.close()
    print("[OK] Gráfico: top_modelos.png")


def generate_conclusions(df: pd.DataFrame) -> None:
    """Genera conclusiones finales."""
    print("\n" + "=" * 50)
    print("  CONCLUSIONES")
    print("=" * 50)

    marca_top = df["marca"].value_counts().index[0]
    modelo_top = df["modelo"].value_counts().index[0] if df["modelo"].notna().any() else "N/A"
    precio_medio = df["precio"].median()

    print(f"\n1. La marca más publicada es: {marca_top}")
    print(f"2. El modelo más frecuente es: {modelo_top}")
    print(f"3. El precio mediano de una moto en Cuba: {precio_medio:,.0f} CUP")

    # Comparación de precios por marca
    precios_marca = df.groupby("marca")["precio"].median().sort_values(ascending=False)
    print(f"\n4. Marca con mayor precio mediano: {precios_marca.index[0]} ({precios_marca.iloc[0]:,.0f} CUP)")
    print(f"   Marca con menor precio mediano: {precios_marca.index[-1]} ({precios_marca.iloc[-1]:,.0f} CUP)")

    # Ubicación
    loc_top = df["ubicacion"].value_counts().index[0]
    print(f"\n5. Provincia con más anuncios: {loc_top}")


def run_analysis(df: pd.DataFrame) -> None:
    """Ejecuta todo el pipeline de análisis."""
    print("\n" + "=" * 50)
    print("  ANÁLISIS DE DATOS")
    print("=" * 50)

    basic_stats(df)
    plot_price_distribution(df)
    plot_top_brands(df)
    plot_price_by_brand(df)
    plot_top_models(df)
    generate_conclusions(df)

    print(f"\n✅ Análisis completado. Gráficos en: {FIGURES_DIR}")


if __name__ == "__main__":
    df = load_clean()
    run_analysis(df)
