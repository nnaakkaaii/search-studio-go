-- psql -U root -d studio < "/commands/update_studio_facility.sql" -v path="'/data/studio - スタジオ設備.csv'"

BEGIN
;

CREATE TEMP TABLE temp_studio_facility(
    studio_facility_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    facility_id INTEGER,
    facility_name VARCHAR,
    studio_facility_serial_number INTEGER,
    studio_facility_description TEXT,
    studio_facility_count INTEGER,
    studio_facility_price FLOAT,
    studio_facility_unit_hour FLOAT
)
;

COPY temp_studio_facility(studio_name, facility_name, studio_facility_serial_number, studio_facility_description, studio_facility_count, studio_facility_price, studio_facility_unit_hour)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

DELETE
FROM
    temp_studio_facility
WHERE
    studio_name IS NULL
OR  facility_name IS NULL
;

UPDATE
    temp_studio_facility
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_studio_facility.studio_name = studio.studio_name
;

DELETE
FROM
    temp_studio_facility
WHERE
    studio_id IS NULL
;

UPDATE
    temp_studio_facility
SET
    facility_id = facility.facility_id
FROM
    facility
WHERE
    temp_studio_facility.facility_name = facility.facility_name
;

DELETE
FROM
    temp_studio_facility
WHERE
    facility_id IS NULL
;

INSERT INTO studio_facility(
    studio_id,
    facility_id,
    studio_facility_serial_number,
    studio_facility_description,
    studio_facility_count,
    studio_facility_price,
    studio_facility_unit_hour,
    created_at,
    is_deleted
)
SELECT
    studio_id,
    facility_id,
    studio_facility_serial_number,
    studio_facility_description,
    studio_facility_count,
    studio_facility_price,
    studio_facility_unit_hour,
    now(),
    false
FROM
    temp_studio_facility
WHERE
    studio_id IS NOT NULL
AND facility_id IS NOT NULL
ON  CONFLICT(studio_id, facility_id, studio_facility_serial_number) DO
    UPDATE
    SET
        studio_facility_description = excluded.studio_facility_description,
        studio_facility_count = excluded.studio_facility_count,
        studio_facility_price = excluded.studio_facility_price,
        studio_facility_unit_hour = excluded.studio_facility_unit_hour,
        updated_at = now()
;

COMMIT
;
