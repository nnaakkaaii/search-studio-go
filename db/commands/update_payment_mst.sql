-- psql -U root -d studio < "/commands/update_payment_mst.sql" -v path="'/data/studio - 支払い方法一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_payment(
    payment_id SERIAL PRIMARY KEY,
    payment_name VARCHAR
)
;

COPY temp_payment(payment_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO payment(
    payment_name
)
SELECT DISTINCT
    payment_name
FROM
    temp_payment
ON  CONFLICT(payment_name) DO NOTHING
;

COMMIT
;
