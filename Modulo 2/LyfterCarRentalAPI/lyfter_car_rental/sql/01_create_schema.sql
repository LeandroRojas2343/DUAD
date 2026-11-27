-- =========================================================
-- 01_create_schema.sql
-- Crea el schema principal del proyecto Lyfter Car Rental.
-- Ejecutar este script PRIMERO, antes que cualquier otro.
-- =========================================================

CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;

-- Todos los objetos de este proyecto se crean dentro de este schema.
-- Fijamos el search_path para la sesion actual para no tener que
-- prefijar cada tabla con "lyfter_car_rental." en el resto de scripts.
SET search_path TO lyfter_car_rental, public;

COMMENT ON SCHEMA lyfter_car_rental IS 'Schema del sistema de alquiler de autos - Lyfter Car Rental';
