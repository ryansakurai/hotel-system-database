-- DDL
CREATE TABLE guest (
    cpf CHAR(14), -- Brazil's Taxpayer Registry for Individuals
    "name" VARCHAR(255),
    phone_number VARCHAR(20) UNIQUE,
    email VARCHAR(255) UNIQUE,

    PRIMARY KEY (cpf)
);

CREATE TABLE hotel (
    "name" VARCHAR(255),
    "address" VARCHAR(255),
    email VARCHAR(255) CHECK (email LIKE '%@%.com'),
    website VARCHAR(255) CHECK (website LIKE 'www.%.com.br'),
    qt_stars INT NOT NULL CHECK (qt_stars>=1 AND qt_stars<=5),

    PRIMARY KEY ("name", "address")
);

CREATE TABLE room (
    hotel_name VARCHAR(255),
    hotel_address VARCHAR(255),
    floor INT,
    "number" INT,
    daily_rate money NOT NULL,
    "type" VARCHAR(14) CHECK ("type" IN ('Single', 'Double Single', 'Couple')),

    PRIMARY KEY (hotel_name, hotel_address, floor, "number"),
    FOREIGN KEY (hotel_name, hotel_address) REFERENCES hotel ("name", "address") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE reservation (
    id INT,
    guest_cpf VARCHAR(14),
    hotel_name VARCHAR(255),
    hotel_address VARCHAR(255),
    room_floor INT,
    room_number INT,
    first_day DATE,
    last_day DATE,

    PRIMARY KEY (id),
    FOREIGN KEY (guest_cpf) REFERENCES guest (cpf) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (hotel_name, hotel_address, room_floor, room_number) REFERENCES room (hotel_name, hotel_address, floor, "number") ON DELETE CASCADE ON UPDATE CASCADE
);


-- TRIGGER
CREATE OR REPLACE FUNCTION check_availability()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM reservation r
        WHERE r.hotel_name = NEW.hotel_name
            AND r.hotel_address = NEW.hotel_address
            AND r.room_floor = NEW.room_floor
            AND r.room_number = NEW.room_number
            AND (NEW.first_day BETWEEN r.first_day AND r.last_day
                OR NEW.last_day BETWEEN r.first_day AND r.last_day)
    ) THEN
        RAISE EXCEPTION 'There''s a conflict with another reservation!';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_availability
BEFORE INSERT ON reservation
FOR EACH ROW
EXECUTE FUNCTION check_availability();


-- ÍNDICES
CREATE INDEX ON hotel (qt_stars);
