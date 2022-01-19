-- psql -U root -d studio < "/commands/update_studio_payment.sql" -v path="'/data/studio - スタジオ支払い方法.csv'"

BEGIN
;

CREATE TEMP TABLE temp_studio_payment(
    studio_payment_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    payment_id INTEGER,
    payment_name VARCHAR
)
;

COPY temp_studio_payment(studio_name, payment_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

UPDATE
    temp_studio_payment
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_studio_payment.studio_name = studio.studio_name
;

DELETE
FROM
    temp_studio_payment
WHERE
    studio_id IS NULL
;

UPDATE
    temp_studio_payment
SET
    payment_id = payment.payment_id
FROM
    payment
WHERE
    temp_studio_payment.payment_name = payment.payment_name
;

DELETE
FROM
    temp_studio_payment
WHERE
    payment_id IS NULL
;

INSERT INTO studio_payment(
    studio_id,
    payment_id,
    created_at,
    is_deleted
)
SELECT
    studio_id,
    payment_id,
    now(),
    false
FROM
    temp_studio_payment
ON  CONFLICT(studio_id, payment_id) DO NOTHING
;

COMMIT
;
