DO $$
DECLARE
    v_bill_id BIGINT := 1;
    v_row     RECORD;
    v_exists  BOOLEAN;
    v_status  TEXT;
BEGIN
    SELECT EXISTS (SELECT 1 FROM shop.bills WHERE id = v_bill_id) INTO v_exists;
    IF NOT v_exists THEN
        RAISE EXCEPTION 'Factura con id % no existe', v_bill_id;
    END IF;

    SELECT status INTO v_status FROM shop.bills WHERE id = v_bill_id FOR UPDATE;

    IF v_status = 'Retornada' THEN
        RAISE EXCEPTION 'La factura % ya ha sido retornada', v_bill_id;
    END IF;

    FOR v_row IN
        SELECT product_id, quantity FROM shop.bill_items WHERE bill_id = v_bill_id
    LOOP
        UPDATE shop.products SET stock = stock + v_row.quantity WHERE id = v_row.product_id;
    END LOOP;

    UPDATE shop.bills SET status = 'Retornada' WHERE id = v_bill_id;
END;
$$;



