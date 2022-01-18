-- psql -U root -d studio < "/commands/update_studio_reservation.sql" -v path="'/data/studio - スタジオ予約方法.csv'"

BEGIN
;

CREATE TEMP TABLE temp_studio_reservation(
    studio_reservation_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    reservation_id INTEGER,
    reservation_name VARCHAR
)
;

COPY temp_studio_reservation(studio_name, reservation_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

UPDATE
    temp_studio_reservation
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_studio_reservation.studio_name = studio.studio_name
;

UPDATE
    temp_studio_reservation
SET
    reservation_id = reservation.reservation_id
FROM
    reservation
WHERE
    temp_studio_reservation.reservation_name = reservation.reservation_name
;

INSERT INTO studio_reservation(
    studio_id,
    reservation_id,
    created_at,
    updated_at,
    is_deleted
)
SELECT
    studio_id,
    reservation_id,
    now(),
    now(),
    false
FROM
    temp_studio_reservation
ON  CONFLICT(studio_id, reservation_id) DO
    UPDATE
    SET
        updated_at = now()
;

COMMIT
;
