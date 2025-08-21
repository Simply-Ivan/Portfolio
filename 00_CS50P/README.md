# 00_fundamentos_python

**Objetivo:** consolidar bases de Python (sintaxis, estructuras de datos y de control, funciones, manejo de archivos) con una introducción práctica a NumPy y pandas.

## Contenido
- `01_sintaxis_elementos_basicos.ipynb`
- `01a_python_exercises.ipynb`
- `02_numpy_vectores.ipynb`
- `03_estructuras_de_datos.ipynb`
- `04_estructuras_de_control.ipynb`
- `05_funciones_y_modulos.ipynb`
- `06_archivos_csv_excel.ipynb`
- `07_trabajo_con_ficheros.ipynb`
- `08_pandas_intro.ipynb`
- `09_data_cleaning.ipynb`
- `dataset/` (archivos de práctica)
- `some_array.npy` (binario de ejemplo)

## Requisitos
Tener instalados Python 3.10+ y `pip`.

## Cómo ejecutar
```bash
# desde la raíz del repo
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r ../requirements.txt
jupyter lab
