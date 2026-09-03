-- =========================================================
-- 05_test_scripts.sql
-- Tarea 2: Pruebas basicas de la DB.
-- Cada bloque es independiente. Reemplace los valores de ejemplo
-- (marcados con <<...>>) por los que necesite probar en pgAdmin
-- (Query Tool). Estos mismos queries son los que luego usa el API
-- de Python en api/db.py.
-- =========================================================

SET search_path TO lyfter_car_rental, public;

-- ---------------------------------------------------------
-- 1. Agregar un usuario nuevo
-- ---------------------------------------------------------
INSERT INTO users (full_name, email, username, password, birth_date, status)
VALUES ('<<Nombre Completo>>', '<<correo@example.com>>', '<<username>>', '<<password>>', '<<1995-05-20>>', 'active')
RETURNING *;

-- ---------------------------------------------------------
-- 2. Agregar un automovil nuevo
-- ---------------------------------------------------------
INSERT INTO cars (brand, model, manufacture_year, status)
VALUES ('<<Toyota>>', '<<Corolla>>', 2022, 'available')
RETURNING *;

-- ---------------------------------------------------------
-- 3. Cambiar el estado de un usuario
-- ---------------------------------------------------------
UPDATE users
SET status = '<<inactive>>'         -- active | inactive | suspended | delinquent
WHERE user_id = <<1>>
RETURNING *;

-- ---------------------------------------------------------
-- 4. Cambiar el estado de un automovil
-- ---------------------------------------------------------
UPDATE cars
SET status = '<<maintenance>>'      -- available | rented | disabled | maintenance
WHERE car_id = <<1>>
RETURNING *;

-- ---------------------------------------------------------
-- 5. Generar un alquiler nuevo con datos de un usuario y un auto
--    (la fecha se autogenera, ademas se marca el auto como "rented")
-- ---------------------------------------------------------
-- 5.a Validar que el auto este disponible antes de alquilar
SELECT status FROM cars WHERE car_id = <<1>>;

-- 5.b Crear el alquiler
INSERT INTO rentals (user_id, car_id, status)
VALUES (<<1>>, <<1>>, 'active')
RETURNING *;

-- 5.c Marcar el auto como alquilado
UPDATE cars SET status = 'rented' WHERE car_id = <<1>>;

-- ---------------------------------------------------------
-- 6. Confirmar la devolucion del auto al completar el alquiler
--    (auto -> available, alquiler -> completed, se llena return_date)
-- ---------------------------------------------------------
UPDATE rentals
SET status = 'completed', return_date = CURRENT_TIMESTAMP
WHERE rental_id = <<1>>
RETURNING *;

UPDATE cars
SET status = 'available'
WHERE car_id = (SELECT car_id FROM rentals WHERE rental_id = <<1>>)
RETURNING *;

-- ---------------------------------------------------------
-- 7. Deshabilitar un automovil del alquiler
--    (regla de negocio: solo se puede deshabilitar si NO esta rented)
-- ---------------------------------------------------------
UPDATE cars
SET status = 'disabled'
WHERE car_id = <<1>>
  AND status <> 'rented'
RETURNING *;

-- ---------------------------------------------------------
-- 8. Obtener todos los automoviles ALQUILADOS
-- ---------------------------------------------------------
SELECT * FROM cars WHERE status = 'rented';

--     Obtener todos los automoviles DISPONIBLES
SELECT * FROM cars WHERE status = 'available';
