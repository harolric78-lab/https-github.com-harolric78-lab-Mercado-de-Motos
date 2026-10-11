# 🏍️ Proyecto: Investigación del Mercado de Motos en Cuba

📋 **Estudiante:** Harold Ricardo Ponce
**Asignatura:** Introducción a la Ciencia de Datos

---

## 🎯 Preguntas de Análisis

1. ¿Cómo está creciendo el mercado de motos eléctricas frente al de combustión?
2. ¿Qué motos tienen precios anormalmente altos?

---

## 📈 Obtención de Datos

| Fuente | Cantidad |
|--------|----------|
| 📢 Sitios de anuncios (Revolico) | ██████████████████████████████ 30 |
| 📝 Encuestas | ██████████████████████████████ 30 |
| 👥 Grupos especializados | 0 |
| 🔧 Importadoras y talleres | ██████████████████████████████ 30 |

---

## 🛠️ Tecnologías Utilizadas

- Python
- Requests
- Jupyter Notebook
- BeautifulSoup (scripts)

---

## 📁 Estructura del Proyecto

```
├── scraping/              → Código de scraping (Revolico)
│   ├── __init__.py
│   └── scraper.py         → Extracción de anuncios
├── src/
│   ├── cleaning.py        → Limpieza y normalización
│   ├── analysis.py        → Gráficos y conclusiones
│   └── generate_comparison.py
├── data/
│   └── comparacion_precios.csv
├── main.py                → Pipeline completo
├── requirements.txt
└── README.md
```
