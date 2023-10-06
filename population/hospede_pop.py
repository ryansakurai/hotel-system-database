import csv
import random

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="proj_hotel",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()


nomes = []

sobrenomes = ['da Silva', 'dos Santos', 'Pereira', 'Alves', 'Ferreira', 'Russo', 'Rodrigues',
              'Gomes', 'Oliveira', 'Ribeiro', 'Martins', 'Gonçalves', 'Soares', 'Barbosa', 'Lopes', 'Vieira',
              'Souza', 'Fernandes', 'Lima', 'Costa', 'Batista', 'Dias', 'Moreira', 'Nunes',
              'Mendes', 'Carvalho', 'Araujo', 'Cardoso', 'Teixeira', 'Marques', 'Teles',
              'Almeida', 'Ramos', 'Machado', 'Rocha', 'Nascimento', 'Pontes', 'Bezerra', 'Sousa',
              'Borges', 'Santana', 'dos Anjos', 'Aparecido', 'Pinto', 'Pinheiro', 'Monteiro', 'Andrade', 'Leite',
              'Correa', 'Nogueira', 'Garcia', 'Henrique', 'Tavares', 'Coelho', 'Pires', 'Queiroz', 'Correia',
              'Miranda', 'de Jesus', 'Duarte', 'Freitas', 'Barros', 'Campos', 'Macedo',
               'Guimaraes', 'Moraes', 'do Carmo', 'dos Reis', 'Viana', 'de Castro', 'Silveira', 'Moura', 'Brito',
              'Neves', 'Carneiro', 'Melo', 'Medeiros', 'Cordeiro', 'Conceição', 'Farias', 'Dantas', 'Cavalcante',
              'de Assis', 'Braga', 'Cruz', 'Siqueira' ]

ddd = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34', '35',
       '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64',
       '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88',
       '89', '91', '92', '93', '94', '95', '96', '97', '98', '99', ]

dominio = ['gmail', 'outlook', 'yahoo', 'mail', 'icloud', 'hotmail']

with open("ibge-mas-10000.csv", "r") as arq:
    arquivo_csv = csv.reader(arq, delimiter=",")
    for linha in arquivo_csv:
        nomes.append(linha[0])

with open("ibge-fem-10000.csv", "r") as arq:
    arquivo_csv = csv.reader(arq, delimiter=",")
    for linha in arquivo_csv:
        nomes.append(linha[0])

nomes.remove("nome")
nomes.remove("nome")

random.shuffle(nomes)

# Nome = nomes + sobrenome
# CPF = numero gerado 11 digitos
# Telefone ddd+9+8 digito random
# Email = p_nome, ult_n + @ dominio

for nome in nomes:
    for sobrenome in sobrenomes:
        try:
            nomao = f'{nome.capitalize()} {sobrenome}'
            cpf = f'{random.randint(30000000000, 99999999999)}'
            tel = f'{random.choice(ddd)} 9{random.randint(10000000, 99999999)}'
            email = f'{nome.lower()}{(sobrenome.split())[-1].lower()}@{random.choice(dominio)}.com'
            cursor.execute("BEGIN;")
            cursor.execute(f"insert into hospede values ('{cpf}', '{nomao}', '{tel}', '{email}')")
            cursor.execute("COMMIT;")
            conn.commit()  # para editar
        except psycopg2.Error as e:
            print(e)
            conn.rollback()




















