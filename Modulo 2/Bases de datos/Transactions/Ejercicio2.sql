DO $$
DECLARE
    v_user_id    BIGINT := 1;
    v_items_json TEXT   := '[{"product_id": 1, "quantity": 2}, {"product_id": 2, "quantity": 1}]';
    v_total      NUMERIC(14,2) := 0;
    v_bill_id    BIGINT;
    v_unit_price NUMERIC(12,2);
    v_stock      INT;
    v_exists     BOOLEAN;
    v_row        RECORD;
BEGIN
    SELECT EXISTS (SELECT 1 FROM shop.users WHERE id = v_user_id) INTO v_exists;
    IF NOT v_exists THEN
        RAISE EXCEPTION 'Usuario con id % no existe', v_user_id;
    END IF;

    FOR v_row IN
        SELECT product_id, quantity
        FROM json_to_recordset(v_items_json) AS x(product_id INT, quantity INT)
    LOOP
        SELECT stock, price INTO v_stock, v_unit_price
        FROM shop.products WHERE id = v_row.product_id
        FOR UPDATE;

        IF NOT FOUND THEN
            RAISE EXCEPTION 'Producto con id % no existe', v_row.product_id;
        END IF;

        IF v_stock < v_row.quantity THEN
            RAISE EXCEPTION 'Stock insuficiente para producto %', v_row.product_id;
        END IF;

        v_total := v_total + (v_unit_price * v_row.quantity);
    END LOOP;

    INSERT INTO shop.bills (user_id, total_amount, status, created_at)
    VALUES (v_user_id, v_total, 'Pagada', NOW())
    RETURNING id INTO v_bill_id;

    FOR v_row IN
        SELECT product_id, quantity
        FROM json_to_recordset(v_items_json) AS x(product_id INT, quantity INT)
    LOOP
        SELECT price INTO v_unit_price FROM shop.products WHERE id = v_row.product_id;

        INSERT INTO shop.bill_items (bill_id, product_id, quantity, unit_price, line_total)
        VALUES (v_bill_id, v_row.product_id, v_row.quantity, v_unit_price, v_unit_price * v_row.quantity);

        UPDATE shop.products SET stock = stock - v_row.quantity WHERE id = v_row.product_id;
    END LOOP;
END;
$$;