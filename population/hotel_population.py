from faker import Faker
from faker.providers import address
import psycopg2
import random

conn = psycopg2.connect(
    host=input("Host: "),
    database=input("Database: "),
    user=input("User: "),
    password=input("Password: ")
)
cursor = conn.cursor()

fake = Faker('pt_BR')
fake.add_provider(address)

NAMES = ('Hotel Grande Vista', 'Pousada do Pôr do Sol', 'Resort Oasis', 'Hotel Palácio Real', 'Hotel Praia Azul', 'Lodge Vista da Montanha', 'Resort Serenidade', 'O Retiro Dourado', 'Hotel Harmonia', 'Resort Paraíso das Palmeiras', 'Pousada Bosque Sussurrante', 'Hotel Estrela Brilhante', 'Resort Refúgio Tranquilo', 'O Hotel Safira', 'Pousada Girassol', 'Lodge Altitude Majestosa', 'Resort Águas Cristalinas', 'Mansão Sob a Luz do Luar', 'Hotel Plaza Nascente', 'Resort Baía Esmeralda', 'Pousada Brisa Costeira', 'Refúgio da Floresta Encantada', 'O Grande Plaza', 'Hotel Refúgio à Beira-Mar', 'Resort Areias de Veludo', 'Lodge Alpino', 'Pousada Jardim das Flores', 'Hotel Mirante do Vale', 'Resort Montanha Serena', 'Pousada Encanto do Mar', 'Hotel Estrela da Manhã', 'Hotel Recanto Verde', 'Pousada Encanto Tropical', 'Lodge Vista do Céu', 'Resort Paraíso Azul', 'Hotel Serra do Sol', 'Pousada Brisa do Mar', 'Oásis no Deserto Hotel', 'Hotel Primavera', 'Resort Encanto da Natureza', 'Pousada Jardim Secreto', 'Hotel Luar Encantado', 'Hotel Rio da Prata', 'Pousada Cachoeira dos Sonhos', 'Resort Montanha Brilhante', 'Pousada Recanto Aconchegante', 'Hotel Flor do Campo', 'Resort Brisa Marítima', 'Pousada Caminho das Estrelas', 'Hotel Canto da Serra')

DOMAINS = ('gmail', 'outlook', 'yahoo', 'mail', 'icloud', 'hotmail')

for name in NAMES:
    email = f"{(name.replace(' ', '')).lower()}@{random.choice(DOMAINS)}.com"
    website = f"www.{(name.replace(' ', '')).lower()}.com.br"
    desired_amount_diff_addresses = random.randint(12, 30) # every chain has 12-30 hotels
    address_counter = 0
    while address_counter < desired_amount_diff_addresses:
        street = fake.street_name()
        number = fake.building_number()
        qt_stars = random.randint(1, 5)
        try:
            cursor.execute("BEGIN;")
            cursor.execute(f"INSERT INTO hotel (\"name\", \"address\", email, website, qt_stars) values ('{name}', '{street}, {number}','{email}','{website}', {qt_stars})")
            cursor.execute("COMMIT;")
            conn.commit()
            address_counter += 1
        except psycopg2.Error as e:
            conn.rollback()
