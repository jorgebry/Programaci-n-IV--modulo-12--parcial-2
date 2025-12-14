#  API REST – Vacunación contra el Sarampión en Panamá

Esta API RESTful de **solo lectura (GET-only)** permite consultar datos históricos sobre la **cobertura de vacunación contra el sarampión en niños de 12 a 23 meses en Panamá**, basados en el indicador **SH.IMM.MEAS** del Banco Mundial.

---

##  Objetivo

Proveer una API pública y reutilizable que permita acceder de forma estructurada a datos históricos de vacunación, sin permitir modificaciones sobre la información.

---

##  Arquitectura

```
Cliente  ⇄  API REST (Flask)  ⇄  Datos en JSON
```

---

##  Estructura del Proyecto

```
vacunas_api/
│
├── app.py
├── data/
│   └── vacunas_panama.json
├── routes/
│   └── vacunas.py
├── tests/
│   └── test_vacunas.py
├── requirements.txt
└── README.md
```

---

## 🔹 Endpoints Disponibles

* **GET /vacunas**
  Devuelve todos los registros disponibles.

* **GET /vacunas/<año>**
  Devuelve el registro correspondiente al año solicitado.

* **GET /vacunas/provincia/<nombre>**
  Devuelve datos simulados por provincia (opcional, con fines académicos).

Todas las respuestas se entregan en formato **JSON**.

---

##  Tecnologías Utilizadas

* Python 3
* Flask
* Datos en formato JSON
* Pytest (pruebas unitarias)

---

##  Ejecución del Proyecto

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la API:

```bash
python app.py
```

La API estará disponible en:

```
http://127.0.0.1:5000
```

---

##  Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest
```

---

##  Restricciones

* La API es **solo de lectura**
* No se permiten métodos POST, PUT o DELETE
* Los datos por provincia son simulados



