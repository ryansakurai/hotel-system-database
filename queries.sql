-- Rank hotels with X stars based on average daily rate
SELECT h.*, AVG(r.daily_rate::numeric)::money AS average_daily_rate
FROM hotel h
    JOIN room q ON r.hotel_name = h.name AND r.hotel_address = h.address
WHERE h.qt_stars = <qtd_X>
GROUP BY h.name, h.address
ORDER BY average_daily_rate DESC;

CREATE OR REPLACE FUNCTION get_hotel_ranking(qt_stars int)
RETURNS TABLE (
    "name" varchar(255),
    "address" varchar(255),
    email varchar(255),
    website varchar(255),
    qt_stars integer,
    average_daily_rate money
) AS $func$
BEGIN
    RETURN QUERY EXECUTE '
        SELECT h.*, AVG(r.diaria::numeric)::money AS average_daily_rate
        FROM hotel h
            JOIN room r ON r.hotel_name = h.name AND r.hotel_address = h.address
        WHERE h.qt_stars = $1
        GROUP BY h.name, h.address
        ORDER BY average_daily_rate DESC
    '
    USING qt_stars;
END
$func$ LANGUAGE plpgsql;


-- Select every guest with last name X who made a reservation in a hotel with Y stars between dates A and B
SELECT g.*, h.name, h.address, h.qt_stars, r.room_floor, r.room_number, r.first_day, r.last_day
FROM guest g
    JOIN reservation r ON r.guest_cpf = g.cpf
    JOIN hotel h ON h.name = r.hotel_name AND h.address = r.hotel_address
WHERE g.name ILIKE '%' || <last_name_x> || '%'
    AND h.qt_stars = <qtd_y>
    AND r.first_day BETWEEN <date_a> AND <date_b>
    AND r.last_day BETWEEN <date_a> AND <date_b>;

CREATE OR REPLACE FUNCTION get_guests(last_name varchar(255), hotel_qt_stars integer, lower_limit date, upper_limit date)
RETURNS TABLE (
    cpf char(14),
    "name" varchar(255),
    phone_number varchar(20),
    email varchar(255),
    hotel_name varchar(255),
    hotel_address varchar(255),
    hotel_qt_stars integer,
    room_floor int,
    room_number int,
    reservation_first_day date,
    reservation_last_day date
) AS $func$
BEGIN
    RETURN QUERY EXECUTE '
        SELECT g.*, h.name, h.address, h.qt_stars, r.room_floor, r.room_number, r.first_day, r.last_day
        FROM guest g
            JOIN reservation r ON r.guest_cpf = g.cpf
            JOIN hotel h ON h.name = r.hotel_name AND h.address = r.hotel_address
        WHERE g.name ILIKE $1
            AND h.qt_stars = $2
            AND r.first_day BETWEEN $3 AND $4
            AND r.last_day BETWEEN $3 AND $4
    '
    USING '%' || last_name || '%', hotel_qt_stars, lower_limit, upper_limit;
END
$func$ LANGUAGE plpgsql;
