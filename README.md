# 🚀 FastAPI + MySQL API

API REST desarrollada con **FastAPI** y conectada a una base de datos **MySQL**, diseñada para consultar estadísticas de pedidos desde la tabla `exq_wc_order_stats`.

---

## 📦 Tecnologías utilizadas

- **FastAPI** – Framework moderno y rápido para APIs en Python
- **Uvicorn** – Servidor ASGI para ejecutar la aplicación
- **MySQL Connector** – Conector oficial para bases de datos MySQL
- **Pydantic** – Validación de datos y modelos

---

## ⚙️ Instalación

1. Clona el repositorio:

git clone https://github.com/CarlosJavier82/fastapi-mysql-api.git cd fastapi-mysql-api

Código

2. Instala las dependencias:

pip install -r requirements.txt

Código

3. Configura tu conexión a MySQL en el archivo `main.py`:

```python
mysql.connector.connect(
    host="TU_HOST",
    user="TU_USUARIO",
    password="TU_PASSWORD",
    database="TU_BASE"
)
Ejecuta el servidor:

Código
uvicorn main:app --reload
📌 Endpoints disponibles
GET /orders
Devuelve los últimos 100 pedidos con:

order_id

order_date

total_sales

📄 Documentación interactiva disponible en: http://localhost:8000/docs

🌐 Despliegue
Este proyecto está listo para ser desplegado en plataformas como Railway o Render. Se recomienda agregar un archivo .env para manejar credenciales y variables de entorno.

📁 Estructura del proyecto
Código
fastapi-mysql-api/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
✍️ Autor
Carlos Vera Backend Developer | FastAPI + MySQL 📧 [Tu correo aquí] 🔗 [Tu LinkedIn o portafolio si deseas]

Código

---

Si quieres que lo personalice aún más con tu correo, LinkedIn o una descripción de tus clientes, solo dime. También puedo ayudarte a preparar el `.env` y el `Procfile` para desplegar tu API en Railway.
