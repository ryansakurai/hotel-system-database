import random
from datetime import date, timedelta
import psycopg2

conn = psycopg2.connect(
    host=input("Host: "),
    database=input("Database: "),
    user=input("User: "),
    password=input("Password: ")
)
cursor = conn.cursor()

cursor.execute(f"select * from room ")
ROOMS = cursor.fetchall()
cursor.execute(f"select * from guest")
GUESTS = cursor.fetchall()

# first day = some day between 2020/01/01 and 2023/07/05
# last day = first day + 0-5 days

LOWER_LIMIT = date(2010, 1, 1)
UPPER_LIMIT = date(2023, 7, 5)
PERIOD = UPPER_LIMIT - LOWER_LIMIT

id = 0
while id < 10000000:
    try:
        guest = random.choice(GUESTS)
        room = random.choice(ROOMS)
        first_day = LOWER_LIMIT + timedelta(days=random.randint(0, PERIOD.days))
        last_day = first_day + timedelta(days=random.randint(0, 5))

        cursor.execute("BEGIN;")
        cursor.execute(f"insert into reservation values ({id},'{guest[0]}','{room[0]}', '{room[1]}', {room[2]}, {room[3]}, '{first_day}', '{last_day}')")
        cursor.execute("COMMIT;")
        conn.commit()
        
        id += 1
    except psycopg2.Error as e:
        print(id)
        print(e)
        conn.rollback()
