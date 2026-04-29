CREATE SCHEMA IF NOT EXISTS shop;

CREATE TABLE IF NOT EXISTS shop.users (
    id         BIGSERIAL PRIMARY KEY,
    username   TEXT UNIQUE NOT NULL,
    email      TEXT UNIQUE NOT NULL,
    full_name  TEXT,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS shop.products (
    id          BIGSERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    description TEXT,
    price       NUMERIC(12,2) NOT NULL CHECK (price >= 0),
    stock       INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
    created_at  TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS shop.bills (
    id           BIGSERIAL PRIMARY KEY,
    user_id      BIGINT REFERENCES shop.users(id) ON DELETE SET NULL,
    total_amount NUMERIC(14,2) NOT NULL,
    status       VARCHAR(20) NOT NULL DEFAULT 'Pagada'
                     CHECK (status IN ('Pagada', 'Retornada', 'Cancelada')),
    created_at   TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS shop.bill_items (
    id         BIGSERIAL PRIMARY KEY,
    bill_id    BIGINT REFERENCES shop.bills(id) ON DELETE CASCADE,
    product_id BIGINT REFERENCES shop.products(id),
    quantity   INT NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12,2) NOT NULL,
    line_total NUMERIC(14,2) NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    UNIQUE (bill_id, product_id)
);