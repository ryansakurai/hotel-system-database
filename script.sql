-- DDL
CREATE TABLE hospede (
    cpf CHAR(14),
    nome VARCHAR(255),
    telefone VARCHAR(20) UNIQUE,
    email VARCHAR(255) UNIQUE,

    PRIMARY KEY (cpf)
);

CREATE TABLE hotel (
    nome VARCHAR(255),
    endereco VARCHAR(255),
    email VARCHAR(255) CHECK (email LIKE '%@%.com'),
    website VARCHAR(255) CHECK (website LIKE 'www.%.com.br'),
    estrelas INT NOT NULL CHECK (estrelas>=1 AND estrelas<=5),

    PRIMARY KEY (nome, endereco)
);

CREATE TABLE quarto (
    hotel_nome VARCHAR(255),
    hotel_endereco VARCHAR(255),
    andar INT,
    numero INT,
    diaria money NOT NULL,
    tipo VARCHAR(14) CHECK (tipo IN ('Solteiro', 'Duplo Solteiro', 'Casal')),

    PRIMARY KEY (hotel_nome, hotel_endereco, andar, numero),
    FOREIGN KEY (hotel_nome, hotel_endereco) REFERENCES hotel (nome, endereco) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE reserva (
    id INT,
    hospede_cpf VARCHAR(14),
    hotel_nome VARCHAR(255),
    hotel_endereco VARCHAR(255),
    quarto_andar INT,
    quarto_numero INT,
    entrada DATE,
    saida DATE,

    PRIMARY KEY (id),
    FOREIGN KEY (hospede_cpf) REFERENCES hospede (cpf) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (hotel_nome, hotel_endereco, quarto_andar, quarto_numero) REFERENCES quarto (hotel_nome, hotel_endereco, andar, numero) ON DELETE CASCADE ON UPDATE CASCADE
);


-- TRIGGER
CREATE OR REPLACE FUNCTION check_availability()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM reserva r
        WHERE r.hotel_nome = NEW.hotel_nome
            AND r.hotel_endereco = NEW.hotel_endereco
            AND r.quarto_andar = NEW.quarto_andar
            AND r.quarto_numero = NEW.quarto_numero
            AND CASE
                    WHEN NEW.entrada BETWEEN r.entrada AND r.saida THEN TRUE
                    WHEN NEW.saida BETWEEN r.entrada AND r.saida THEN TRUE
                    ELSE FALSE
                END
    ) THEN
        RAISE EXCEPTION 'Conflito com outra reserva!';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_availability
BEFORE INSERT ON reserva
FOR EACH ROW
EXECUTE FUNCTION check_availability();


-- ÍNDICES
CREATE INDEX ON hotel (estrelas);
