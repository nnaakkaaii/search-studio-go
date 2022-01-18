-- psql -U root -d studio < "/commands/update_room_facility.sql" -v path="'/data/studio - 部屋設備.csv'"

BEGIN
;

CREATE TEMP TABLE temp_room_facility(
    room_facility_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    room_id INTEGER,
    room_name VARCHAR,
    facility_id INTEGER,
    facility_name VARCHAR,
    room_facility_serial_number INTEGER,
    room_facility_count INTEGER,
    room_facility_price FLOAT,
    room_facility_unit_hour FLOAT
)
;

COPY temp_room_facility(studio_name, room_name, facility_name, room_facility_serial_number, room_facility_count, room_facility_price, room_facility_unit_hour)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

UPDATE
    temp_room_facility
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_room_facility.studio_name = studio.studio_name
;

UPDATE
    temp_room_facility
SET
    room_id = room.room_id
FROM
    room
WHERE
    temp_room_facility.studio_id = room.studio_id
    AND temp_room_facility.room_name = room.room_name
;

UPDATE
    temp_room_facility
SET
    facility_id = facility.facility_id
FROM
    facility
WHERE
    temp_room_facility.facility_name = facility.facility_name
;

INSERT INTO room_facility(
    room_id,
    facility_id,
    room_facility_serial_number,
    room_facility_count,
    room_facility_price,
    room_facility_unit_hour,
    created_at,
    updated_at,
    is_deleted
)
SELECT
    room_id,
    facility_id,
    room_facility_serial_number,
    room_facility_count,
    room_facility_price,
    room_facility_unit_hour,
    now(),
    now(),
    false
FROM
    temp_room_facility
ON  CONFLICT(room_id, facility_id, room_facility_serial_number) DO
    UPDATE
    SET
        room_facility_count = temp_room_facility.room_facility_count,
        room_facility_price = temp_room_facility.room_facility_price,
        room_facility_unit_hour = temp_room_facility.room_facility_unit_hour,
        updated_at = now()
;

COMMIT
;
