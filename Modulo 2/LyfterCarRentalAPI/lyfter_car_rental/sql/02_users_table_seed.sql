-- =========================================================
-- 02_users_table_seed.sql
-- Crea la tabla de usuarios y la puebla con 50 usuarios falsos.
-- Un solo script: se ejecuta una vez y deja la tabla creada y poblada.
-- =========================================================

SET search_path TO lyfter_car_rental, public;

-- -------------------------------------------------
-- 1. Tabla de usuarios
-- -------------------------------------------------
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    user_id         SERIAL PRIMARY KEY,                 -- ID unico autoincremental
    full_name       VARCHAR(150)  NOT NULL,
    email           VARCHAR(150)  NOT NULL UNIQUE,
    username        VARCHAR(50)   NOT NULL UNIQUE,
    password        VARCHAR(255)  NOT NULL,
    birth_date      DATE          NOT NULL,
    status          VARCHAR(20)   NOT NULL DEFAULT 'active',
    created_at      TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_users_status CHECK (status IN ('active', 'inactive', 'suspended', 'delinquent'))
);

COMMENT ON COLUMN users.status IS 'active | inactive | suspended | delinquent (moroso)';

-- -------------------------------------------------
-- 2. Poblado con 50 usuarios generados aleatoriamente
-- -------------------------------------------------
DO $$
DECLARE
    first_names TEXT[] := ARRAY['Maria','Jose','Carlos','Ana','Luis','Laura','Diego','Sofia',
                                 'Andres','Valeria','Jorge','Camila','Pedro','Daniela','Miguel',
                                 'Fernanda','Ricardo','Paula','Kevin','Gabriela','Esteban','Monica',
                                 'Alejandro','Natalia','Roberto','Karla','Fabian','Melissa','Ivan',
                                 'Priscilla'];
    last_names  TEXT[] := ARRAY['Rodriguez','Gonzalez','Mora','Jimenez','Vargas','Castro','Solis',
                                 'Chacon','Alvarado','Barrantes','Vega','Rojas','Fernandez','Salas',
                                 'Quiros','Zamora','Arias','Aguilar','Chavarria','Blanco'];
    statuses    TEXT[] := ARRAY['active','active','active','active','inactive','suspended'];
    v_first     TEXT;
    v_last      TEXT;
    v_username  TEXT;
    v_email     TEXT;
    i           INT;
BEGIN
    FOR i IN 1..50 LOOP
        v_first    := first_names[1 + floor(random() * array_length(first_names, 1))::int];
        v_last     := last_names[1 + floor(random() * array_length(last_names, 1))::int];
        v_username := lower(v_first) || lower(v_last) || i::text;
        v_email    := v_username || '@example.com';

        INSERT INTO users (full_name, email, username, password, birth_date, status)
        VALUES (
            v_first || ' ' || v_last,
            v_email,
            v_username,
            md5(v_username || 'pwd'),                                   -- password "hasheado" ficticio
            (DATE '1970-01-01' + (random() * 365 * 35)::int)::date,     -- fecha de nacimiento aleatoria entre 1970-2005
            statuses[1 + floor(random() * array_length(statuses, 1))::int]
        );
    END LOOP;
END $$;

-- Verificacion rapida
SELECT COUNT(*) AS total_usuarios FROM users;
