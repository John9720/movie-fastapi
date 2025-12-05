# Movie API con FastAPI

API REST construida con **FastAPI** que permite gestionar una biblioteca de películas.
Incluye operaciones CRUD completas, autenticación con **JWT** y manejo de base de datos mediante **SQLAlchemy**.

---

## 🚀 Características

- CRUD de películas (crear, leer, actualizar, eliminar).
- Autenticación basada en JWT.
- Validación automática de datos con Pydantic.
- Respuestas rápidas gracias a FastAPI.
- Integración con SQLAlchemy para manejar la base de datos.

---

## 🛠️ Tecnologías usadas

- FastAPI
- SQLAlchemy
- PyJWT
- Uvicorn

---

## 📁 Estructura del proyecto (ejemplo)

FastAPI/
├── db/
│   ├── __init__.py          # Permite tratar la carpeta como un módulo
│   ├── database.py          # Configuración de la base de datos (SQLAlchemy)
│   └── movies.sqlite        # Base de datos SQLite del proyecto
│
├── models/
│   └── movies.py            # Modelos ORM usados por SQLAlchemy
│
├── routers/
│   ├── __init__.py          # Permite importar los routers como módulo
│   ├── movie.py             # Endpoints relacionados con películas
│   └── users.py             # Endpoints relacionados con usuarios
│
├── main.py                  # Archivo principal, crea la app y agrega los routers
├── user_jwt.py              # Utilidades para manejo de JWT (tokens/seguridad)
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación del proyecto


---

## 🔐 Autenticación

Esta API utiliza **JWT**.
Para acceder a uno de los endpoints:

1. Obtener un token en `/login`
2. En esta implementación, las credenciales están definidas de manera estática dentro del código, únicamente con fines de demostración.



---

## ⚙️ Cómo ejecutar el proyecto localmente

### 1. Clonar el repositorio

git clone https://github.com/John9720/movie-fastapi
cd movie-fastapi

## 2. Crear un entorno virtual 

python3 -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

## 3. Instalar dependencias

pip install -r requirements.txt

## 4. Ejecutar la API

uvicorn main:app --realod

## 5. Abrir documentación

http://localhost:8000/docs


---

## 📝 Notas

Este proyecto muestra mi experiencia creando APIs con FastAPI, JWT y SQLAlchemy.
