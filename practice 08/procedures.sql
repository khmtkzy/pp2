CREATE OR REPLACE PROCEDURE upsert_u(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO phonebook (username, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (username)
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$;

CREATE OR REPLACE PROCEDURE loophz(p_user VARCHAR[], p_phone VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    IF array_length(p_user, 1) IS DISTINCT FROM array_length(p_phone, 1) THEN
        RAISE EXCEPTION 'Arrays must have the same length';
    END IF;

    FOR i IN 1..array_length(p_user, 1) LOOP
        IF p_phone[i] !~ '^[0-9]+$' THEN
            RAISE NOTICE 'Invalid row -> username: %, phone: %', p_user[i], p_phone[i];
        ELSIF p_user[i] ~ '[0-9]' THEN
            RAISE NOTICE 'Invalid row -> username: %, phone: %', p_user[i], p_phone[i];
        ELSE
            CALL upsert_u(p_user[i], p_phone[i]);
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE del_user(p VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p OR phone = p;
END;
$$;