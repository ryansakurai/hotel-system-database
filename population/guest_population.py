import csv
import random
import psycopg2

conn = psycopg2.connect(
    host=input("Host: "),
    database=input("Database: "),
    user=input("User: "),
    password=input("Password: ")
)
cursor = conn.cursor()

first_names = []
with open("brazilian-names/ibge-mas-10000.csv", "r") as file:
    csv_file = csv.reader(file, delimiter=",")
    for line in csv_file:
        first_names.append(line[0])
first_names.remove("nome")
with open("brazilian-names/ibge-fem-10000.csv", "r") as file:
    csv_file = csv.reader(file, delimiter=",")
    for line in csv_file:
        first_names.append(line[0])
first_names.remove("nome")
FIRST_NAMES = tuple(first_names)

LAST_NAMES = ('da Silva', 'dos Santos', 'Pereira', 'Alves', 'Ferreira', 'Russo', 'Rodrigues', 'Gomes', 'Oliveira', 'Ribeiro', 'Martins', 'Gonçalves', 'Soares', 'Barbosa', 'Lopes', 'Vieira', 'Souza', 'Fernandes', 'Lima', 'Costa', 'Batista', 'Dias', 'Moreira', 'Nunes', 'Mendes', 'Carvalho', 'Araujo', 'Cardoso', 'Teixeira', 'Marques', 'Teles', 'Almeida', 'Ramos', 'Machado', 'Rocha', 'Nascimento', 'Pontes', 'Bezerra', 'Sousa', 'Borges', 'Santana', 'dos Anjos', 'Aparecido', 'Pinto', 'Pinheiro', 'Monteiro', 'Andrade', 'Leite', 'Correa', 'Nogueira', 'Garcia', 'Henrique', 'Tavares', 'Coelho', 'Pires', 'Queiroz', 'Correia', 'Miranda', 'de Jesus', 'Duarte', 'Freitas', 'Barros', 'Campos', 'Macedo', 'Guimaraes', 'Moraes', 'do Carmo', 'dos Reis', 'Viana', 'de Castro', 'Silveira', 'Moura', 'Brito', 'Neves', 'Carneiro', 'Melo', 'Medeiros', 'Cordeiro', 'Conceição', 'Farias', 'Dantas', 'Cavalcante', 'de Assis', 'Braga', 'Cruz', 'Siqueira')

AREA_CODE = ('11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99')

DOMAIN = ('gmail', 'outlook', 'yahoo', 'mail', 'icloud', 'hotmail')

DESIRED_QT_GUESTS = input("Quantity of guests: ")

# CPF = random 11 digit numbers between 30,000,000,000 and 99,999,999,999
# Name = first name + last name
# Phone number = area code + "9" + random 8 digit number
# Email = first name + last name + random number + @ + DOMAIN + ".com"

guest_count = 0
while guest_count <= DESIRED_QT_GUESTS:
    try:
        cpf = str(random.randint(30000000000, 99999999999))
        first_name = random.choice(FIRST_NAMES).capitalize()
        last_name = random.choice(LAST_NAMES)
        name = f'{first_name} {last_name}'
        phone_number = f'{random.choice(AREA_CODE)} 9{random.randint(10000000, 99999999)}'
        email = f'{first_name.lower()}.{(last_name.split())[-1].lower()}{random.randint(0, 99)}@{random.choice(DOMAIN)}.com'
        cursor.execute("BEGIN;")
        cursor.execute(f"insert into guest values ('{cpf}', '{name}', '{phone_number}', '{email}')")
        cursor.execute("COMMIT;")
        conn.commit()
        guest_count += 1
    except psycopg2.Error as e:
        continue
