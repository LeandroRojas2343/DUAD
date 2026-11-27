-- =========================================================
-- 04_rentals_table.sql
-- Crea la tabla cruz "rentals" que relaciona usuarios y autos.
-- Requiere que 02_users_table_seed.sql y 03_cars_table_seed.sql
-- ya hayan sido ejecutados (necesita las FKs).
-- =========================================================

SET search_path TO lyfter_car_rental, public;

DROP TABLE IF EXISTS rentals CASCADE;

CREATE TABLE rentals (
    rental_id       SERIAL PRIMARY KEY,
    user_id         INT NOT NULL REFERENCES users(user_id),
    car_id          INT NOT NULL REFERENCES cars(car_id),
    rental_date     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- autogenerada al insertar
    return_date     TIMESTAMP NULL,                                -- se llena al completar el alquiler
    status          VARCHAR(20) NOT NULL DEFAULT 'active',
    CONSTRAINT chk_rentals_status CHECK (status IN ('active', 'completed', 'cancelled'))
);

COMMENT ON COLUMN rentals.status IS 'active | completed | cancelled';
COMMENT ON COLUMN rentals.rental_date IS 'Se autogenera al momento de crear el alquiler';

-- Indices utiles para las consultas de listado con filtros
CREATE INDEX idx_rentals_user_id ON rentals(user_id);
CREATE INDEX idx_rentals_car_id  ON rentals(car_id);
CREATE INDEX idx_rentals_status  ON rentals(status);
