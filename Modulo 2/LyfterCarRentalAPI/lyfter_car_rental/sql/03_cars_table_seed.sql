-- =========================================================
-- 03_cars_table_seed.sql
-- Crea la tabla de automoviles y la puebla con 30 autos falsos.
-- Un solo script: se ejecuta una vez y deja la tabla creada y poblada.
-- =========================================================

SET search_path TO lyfter_car_rental, public;

-- -------------------------------------------------
-- 1. Tabla de automoviles
-- -------------------------------------------------
DROP TABLE IF EXISTS cars CASCADE;

CREATE TABLE cars (
    car_id          SERIAL PRIMARY KEY,                 -- ID unico autoincremental
    brand           VARCHAR(50)  NOT NULL,
    model           VARCHAR(50)  NOT NULL,
    manufacture_year INT         NOT NULL,
    status          VARCHAR(20)  NOT NULL DEFAULT 'available',
    created_at      TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_cars_status CHECK (status IN ('available', 'rented', 'disabled', 'maintenance')),
    CONSTRAINT chk_cars_year CHECK (manufacture_year BETWEEN 1980 AND 2100)
);

COMMENT ON COLUMN cars.status IS 'available | rented | disabled | maintenance';

-- -------------------------------------------------
-- 2. Poblado con 30 automoviles generados aleatoriamente
-- -------------------------------------------------
DO $$
DECLARE
    brands  TEXT[] := ARRAY['Toyota','Hyundai','Kia','Honda','Nissan','Chevrolet','Ford','Mazda','Suzuki','Volkswagen'];
    models  TEXT[] := ARRAY['Corolla','Rav4','Tucson','Elantra','Rio','Civic','CRV','Sentra','Kicks','Spark',
                             'Onix','Fiesta','Ecosport','3','CX5','Swift','Vitara','Jetta','Tiguan','Yaris'];
    statuses TEXT[] := ARRAY['available','available','available','available','maintenance'];
    i INT;
BEGIN
    FOR i IN 1..30 LOOP
        INSERT INTO cars (brand, model, manufacture_year, status)
        VALUES (
            brands[1 + floor(random() * array_length(brands, 1))::int],
            models[1 + floor(random() * array_length(models, 1))::int],
            2012 + floor(random() * 13)::int,   -- anio entre 2012 y 2024
            statuses[1 + floor(random() * array_length(statuses, 1))::int]
        );
    END LOOP;
END $$;

-- Verificacion rapida
SELECT COUNT(*) AS total_autos FROM cars;
