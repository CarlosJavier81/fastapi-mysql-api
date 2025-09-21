from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel
from typing import List

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
        host="TU_HOST",
        user="TU_USUARIO",
        password="TU_PASSWORD",
        database="TU_BASE"
    )

class Order(BaseModel):
    order_id: int
    order_date: str
    total_sales: float

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