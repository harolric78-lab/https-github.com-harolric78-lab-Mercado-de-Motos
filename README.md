# 🏍️ Proyecto: Análisis del Mercado de Motos en Cuba

**Harold Ricardo Ponce**
**Introducción a la Ciencia de Datos**

**Rol:** Analista de motos

---

## Objetivo

Analizar el mercado de motocicletas en Cuba mediante técnicas de ciencia de datos, desde la extracción de anuncios hasta la generación de conclusiones.

---

## Preguntas de Investigación

- ¿Cuál es la moto más vendida en Cuba?
- ¿Qué marcas dominan el mercado cubano?
- ¿Cómo varían los precios entre motos eléctricas, de combustión y patinetes?

---

## Comparación de Precios Promedio (CUP)

| Tipo | Promedio | Cantidad |
|------|----------|----------|
| Combustión | 13,880 | 10 |
| Eléctrica | 4,240 | 10 |
| Patinete | 3,180 | 10 |

> Datos completos en `data/comparacion_precios.csv`

---

## Metodología

| Fase | Técnica | Herramienta |
|------|---------|-------------|
| Extracción | Web Scraping | BeautifulSoup + Requests |
| Limpieza | Duplicados, normalización | Pandas |
| Análisis | Estadísticas descriptivas | Pandas |
| Visualización | Histogramas, boxplots | Matplotlib + Seaborn |

---

## Ejecución

```bash
pip install -r requirements.txt
python main.py
```
