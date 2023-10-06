-- criação de roles
CREATE ROLE administrador SUPERUSER;
CREATE ROLE gerente;
CREATE ROLE atendente; 
CREATE ROLE cliente;
CREATE ROLE anonimo;

ALTER DATABASE rede_hoteis OWNER TO administrador;

SET ROLE administrador;

-- concessões em hospede
GRANT SELECT ON hospede TO gerente;
GRANT SELECT ON hospede TO atendente;
GRANT SELECT, INSERT, UPDATE, DELETE ON hospede TO cliente;

-- concessões em hotel
GRANT SELECT, UPDATE(email, website) ON hotel TO gerente;
GRANT SELECT ON hotel TO atendente;
GRANT SELECT ON hotel TO cliente;
GRANT SELECT ON hotel TO anonimo;

-- concessões em quarto
GRANT SELECT, INSERT, UPDATE(diaria, tipo), DELETE ON quarto TO gerente;
GRANT SELECT ON quarto TO atendente;
GRANT SELECT ON quarto TO cliente;
GRANT SELECT ON quarto TO anonimo;

-- concessões em reserva
GRANT SELECT ON reserva TO gerente;
GRANT SELECT, INSERT, UPDATE, DELETE ON reserva TO atendente;
GRANT SELECT ON reserva TO cliente;
