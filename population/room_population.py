import random
import psycopg2

conn = psycopg2.connect(
    host=input("Host: "),
    database=input("Database: "),
    user=input("User: "),
    password=input("Password: ")
)
cursor = conn.cursor()

TYPES = ("Single", "Double Single", "Couple")

PRICE_RANGES = {
    "Single": {
        "LOWER_LIMIT": 50,
        "UPPER_LIMIT": 150
    },
    "Double Single": {
        "LOWER_LIMIT": 250,
        "UPPER_LIMIT": 350
    },
    "Couple": {
        "LOWER_LIMIT": 400,
        "UPPER_LIMIT": 500
    }
}

cursor.execute(f"select * from hotel")
hotels = cursor.fetchall()

# daily rate = number between lower and upper limit * qt_stars

for hotel in hotels:
    qt_floors = random.randint(6, 15)
    qt_rooms_per_floor = random.randint(10, 15)
    for floor in range(0, qt_floors):
        for number in range(0, qt_rooms_per_floor):
            try:
                room_type = random.choice(TYPES)
                daily_rate = random.randint(PRICE_RANGES[room_type]["LOWER_LIMIT"], PRICE_RANGES[room_type]["UPPER_LIMIT"]) * hotel[-1]
                cursor.execute("BEGIN;")
                cursor.execute(f"insert into room values ('{hotel[0]}','{hotel[1]}', {floor}, {number}, {daily_rate}, '{room_type}')")
                cursor.execute("COMMIT;")
                conn.commit()
            except psycopg2.Error as e:
                print(e)
                conn.rollback()
