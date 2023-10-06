from random import randint, choice
from datetime import date, timedelta
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="proj_hotel",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()
cursor.execute(f"select * from quarto ")
QUARTOS = cursor.fetchall()
cursor.execute(f"select * from hospede")
HOSPEDES = cursor.fetchall()

DATA_INICIAL = date(2010, 1, 1)
DATA_FINAL = date(2023, 7, 5)
PERIODO_COMPLETO = DATA_FINAL - DATA_INICIAL
id = 0
while id < 10000000:
    try:
        hosp = choice(HOSPEDES)
        qua = choice(QUARTOS)

        qt_aleatoria = randint(0, PERIODO_COMPLETO.days)
        inicio = DATA_INICIAL + timedelta(days=qt_aleatoria)
        fim = inicio + timedelta(days=randint(0, 5))

        cursor.execute("BEGIN;")
        cursor.execute(f"insert into reserva values ({id},'{hosp[0]}','{qua[0]}', '{qua[1]}', {qua[2]}, {qua[3]}, '{inicio}', '{fim}')")
        cursor.execute("COMMIT;")
        conn.commit()
        id += 1
    except psycopg2.Error as e:
        print(id)
        print(e)
        conn.rollback()
