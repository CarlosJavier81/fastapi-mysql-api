import mysql.connector
from fastapi import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import mysql.connector
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (solo útil en local)
load_dotenv()

app = FastAPI()

# Modelo de datos para el endpoint /orders
class Order(BaseModel):
    order_id: int
    order_date: str
    total_sales: float

# Función para conectar a la base de datos usando variables de entorno
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port = int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME")
    )

# Endpoint principal
@app.get("/orders", response_model=List[Order])
def get_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT order_id, DATE(date_created) AS order_date, total_sales
        FROM exq_wc_order_stats
        ORDER BY date_created DESC
        LIMIT 100
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Order(order_id=r[0], order_date=str(r[1]), total_sales=float(r[2])) for r in rows]
