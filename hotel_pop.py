from faker import Faker
from faker.providers import address
import psycopg2
from random import choice, randint

conn = psycopg2.connect(
    host="localhost",
    database="proj_hotel",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()


fake = Faker('pt_BR')
fake.add_provider(address)


# Gerar um endereço completo

# Nome
# Endereco
# Email
# Site
# Estrelas


nomes = ['Hotel Grande Vista', 'Pousada do Pôr do Sol', 'Resort Oasis', 'Hotel Palácio Real', 'Hotel Praia Azul', 'Lodge Vista da Montanha', 'Resort Serenidade', 'O Retiro Dourado', 'Hotel Harmonia', 'Resort Paraíso das Palmeiras', 'Pousada Bosque Sussurrante', 'Hotel Estrela Brilhante', 'Resort Refúgio Tranquilo', 'O Hotel Safira', 'Pousada Girassol', 'Lodge Altitude Majestosa', 'Resort Águas Cristalinas', 'Mansão Sob a Luz do Luar', 'Hotel Plaza Nascente', 'Resort Baía Esmeralda', 'Pousada Brisa Costeira', 'Refúgio da Floresta Encantada', 'O Grande Plaza', 'Hotel Refúgio à Beira-Mar', 'Resort Areias de Veludo', 'Lodge Alpino', 'Pousada Jardim das Flores', 'Hotel Mirante do Vale', 'Resort Montanha Serena', 'Pousada Encanto do Mar', 'Hotel Estrela da Manhã', 'Hotel Recanto Verde', 'Pousada Encanto Tropical', 'Lodge Vista do Céu', 'Resort Paraíso Azul', 'Hotel Serra do Sol', 'Pousada Brisa do Mar', 'Oásis no Deserto Hotel', 'Hotel Primavera', 'Resort Encanto da Natureza', 'Pousada Jardim Secreto', 'Hotel Luar Encantado', 'Hotel Rio da Prata', 'Pousada Cachoeira dos Sonhos', 'Resort Montanha Brilhante', 'Pousada Recanto Aconchegante', 'Hotel Flor do Campo', 'Resort Brisa Marítima', 'Pousada Caminho das Estrelas', 'Hotel Canto da Serra']
dominio = ['gmail', 'outlook', 'yahoo', 'mail', 'icloud', 'hotmail']


for hotel in nomes:
    email = f"{(hotel.replace(' ', '')).lower()}@{choice(dominio)}.com"
    site = f"www.{(hotel.replace(' ', '')).lower()}.com.br"
    for c in range(randint(12, 30)):
        num = fake.building_number()
        rua = fake.street_name()
        estrelas = randint(1, 5)
        try:
            cursor.execute("BEGIN;")
            cursor.execute(f"insert into hotel (nome, endereco, email, website, estrelas) values ('{hotel}', '{rua}, {num}','{email}','{site}', {estrelas})")
            cursor.execute("COMMIT;")
            conn.commit()  # para editar
        except psycopg2.Error as e:
            print(e)
            conn.rollback()




















