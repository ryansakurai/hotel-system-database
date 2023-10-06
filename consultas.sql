-- Mostre um ranking de hotéis de número de estrelas X com base no preço médio da diária
SELECT h.*, AVG(q.diaria::numeric)::money AS diaria_media
FROM hotel h
    JOIN quarto q ON q.hotel_nome = h.nome AND q.hotel_endereco = h.endereco
WHERE h.estrelas = <qtd_X>
GROUP BY h.nome, h.endereco
ORDER BY diaria_media DESC;

CREATE OR REPLACE FUNCTION get_ranking_hoteis(qt_estrelas int)
RETURNS TABLE (
    nome varchar(255),
    endereco varchar(255),
    email varchar(255),
    website varchar(255),
    estrelas integer,
    diaria_media money
) AS $func$
BEGIN
    RETURN QUERY EXECUTE '
        SELECT h.*, AVG(q.diaria::numeric)::money AS diaria_media
        FROM hotel h
            JOIN quarto q ON q.hotel_nome = h.nome AND q.hotel_endereco = h.endereco
        WHERE h.estrelas = $1
        GROUP BY h.nome, h.endereco
        ORDER BY diaria_media DESC
    '
    USING qt_estrelas;
END
$func$ LANGUAGE plpgsql;


-- Recupere todos os hóspedes de sobrenome X que fizeram reserva em hotéis com quantidade de estrelas Y entre as datas A e B
SELECT hos.*, hot.nome, hot.endereco, hot.estrelas, r.quarto_andar, r.quarto_numero, r.entrada, r.saida
FROM hospede hos
    JOIN reserva r ON r.hospede_cpf = hos.cpf
    JOIN hotel hot ON hot.nome = r.hotel_nome AND hot.endereco = r.hotel_endereco
WHERE hos.nome ILIKE '%' || <sobrenome_x> || '%'
    AND hot.estrelas = <qtd_y>
    AND r.entrada BETWEEN <data_a> AND <data_b>
    AND r.saida BETWEEN <data_a> AND <data_b>;

CREATE OR REPLACE FUNCTION get_hospedes(sobrenome varchar(255), estrelas_hotel integer, limite_inf date, limite_post date)
RETURNS TABLE (
    cpf char(14),
    nome varchar(255),
    telefone varchar(20),
    email varchar(255),
    hotel_nome varchar(255),
    hotel_endereco varchar(255),
    hotel_estrelas integer,
    quarto_andar int,
    quarto_numero int,
    reserva_entrada date,
    reserva_saida date
) AS $func$
BEGIN
    RETURN QUERY EXECUTE '
        SELECT hos.*, hot.nome, hot.endereco, hot.estrelas, r.quarto_andar, r.quarto_numero, r.entrada, r.saida
        FROM hospede hos
            JOIN reserva r ON r.hospede_cpf = hos.cpf
            JOIN hotel hot ON hot.nome = r.hotel_nome AND hot.endereco = r.hotel_endereco
        WHERE hos.nome ILIKE $1
            AND hot.estrelas = $2
            AND r.entrada BETWEEN $3 AND $4
            AND r.saida BETWEEN $3 AND $4
    '
    USING '%' || sobrenome || '%', estrelas_hotel, limite_inf, limite_post;
END
$func$ LANGUAGE plpgsql;
