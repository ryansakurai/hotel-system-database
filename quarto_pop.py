from random import randint, choice
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="proj_hotel",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()
nomes = ['Hotel Grande Vista', 'Pousada do Pôr do Sol', 'Resort Oasis', 'Hotel Palácio Real', 'Hotel Praia Azul', 'Lodge Vista da Montanha', 'Resort Serenidade', 'O Retiro Dourado', 'Hotel Harmonia', 'Resort Paraíso das Palmeiras', 'Pousada Bosque Sussurrante', 'Hotel Estrela Brilhante', 'Resort Refúgio Tranquilo', 'O Hotel Safira', 'Pousada Girassol', 'Lodge Altitude Majestosa', 'Resort Águas Cristalinas', 'Mansão Sob a Luz do Luar', 'Hotel Plaza Nascente', 'Resort Baía Esmeralda', 'Pousada Brisa Costeira', 'Refúgio da Floresta Encantada', 'O Grande Plaza', 'Hotel Refúgio à Beira-Mar', 'Resort Areias de Veludo', 'Lodge Alpino', 'Pousada Jardim das Flores', 'Hotel Mirante do Vale', 'Resort Montanha Serena', 'Pousada Encanto do Mar', 'Hotel Estrela da Manhã', 'Hotel Recanto Verde', 'Pousada Encanto Tropical', 'Lodge Vista do Céu', 'Resort Paraíso Azul', 'Hotel Serra do Sol', 'Pousada Brisa do Mar', 'Oásis no Deserto Hotel', 'Hotel Primavera', 'Resort Encanto da Natureza', 'Pousada Jardim Secreto', 'Hotel Luar Encantado', 'Hotel Rio da Prata', 'Pousada Cachoeira dos Sonhos', 'Resort Montanha Brilhante', 'Pousada Recanto Aconchegante', 'Hotel Flor do Campo', 'Resort Brisa Marítima', 'Pousada Caminho das Estrelas', 'Hotel Canto da Serra']
tipo = ['Solteiro', 'Duplo Solteiro', 'Casal']
preco_qua = {'Solteiro': (50, 150), 'Duplo Solteiro': (250, 350), 'Casal': (400, 500)}
cursor.execute(f"select * from hotel")
hoteis = cursor.fetchall()

for hotel in hoteis:
    quartos = randint(10, 15)
    for c in range(0, randint(6, 15)):
        for n in range(0, quartos):
            try:
                tipo_quarto = choice(tipo)
                preco = randint(preco_qua[tipo_quarto][0], preco_qua[tipo_quarto][1]) * hotel[-1]
                cursor.execute("BEGIN;")
                cursor.execute(f"insert into quarto values ('{hotel[0]}','{hotel[1]}', {c}, {n}, {preco}, '{tipo_quarto}')")
                cursor.execute("COMMIT;")
                conn.commit()  # para editar
            except psycopg2.Error as e:
                print(e)
                conn.rollback()





















