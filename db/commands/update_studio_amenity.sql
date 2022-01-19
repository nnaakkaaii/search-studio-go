-- psql -U root -d studio < "/commands/update_studio_amenity.sql" -v path="'/data/studio - スタジオアメニティ.csv'"

BEGIN
;

CREATE TEMP TABLE temp_studio_amenity(
    studio_amenity_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    amenity_id INTEGER,
    amenity_name VARCHAR,
    studio_amenity_serial_number INTEGER,
    studio_amenity_description TEXT,
    studio_amenity_count INTEGER,
    studio_amenity_price FLOAT,
    studio_amenity_unit_hour FLOAT
)
;

COPY temp_studio_amenity(studio_name, amenity_name, studio_amenity_serial_number, studio_amenity_description, studio_amenity_count, studio_amenity_price, studio_amenity_unit_hour)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

DELETE
FROM
    temp_studio_amenity
WHERE
    studio_name IS NULL
OR  amenity_name IS NULL
;

UPDATE
    temp_studio_amenity
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_studio_amenity.studio_name = studio.studio_name
;

DELETE
FROM
    temp_studio_amenity
WHERE
    studio_id IS NULL
;

UPDATE
    temp_studio_amenity
SET
    amenity_id = amenity.amenity_id
FROM
    amenity
WHERE
    temp_studio_amenity.amenity_name = amenity.amenity_name
;

DELETE
FROM
    temp_studio_amenity
WHERE
    amenity_id IS NULL
;

INSERT INTO studio_amenity(
    studio_id,
    amenity_id,
    studio_amenity_serial_number,
    studio_amenity_description,
    studio_amenity_count,
    studio_amenity_price,
    studio_amenity_unit_hour,
    created_at,
    is_deleted
)
SELECT
    studio_id,
    amenity_id,
    studio_amenity_serial_number,
    studio_amenity_description,
    studio_amenity_count,
    studio_amenity_price,
    studio_amenity_unit_hour,
    now(),
    false
FROM
    temp_studio_amenity
ON  CONFLICT(studio_id, amenity_id, studio_amenity_serial_number) DO
    UPDATE
    SET
        studio_amenity_description = excluded.studio_amenity_description,
        studio_amenity_count = excluded.studio_amenity_count,
        studio_amenity_price = excluded.studio_amenity_price,
        studio_amenity_unit_hour = excluded.studio_amenity_unit_hour,
        updated_at = now()
;

COMMIT
;
