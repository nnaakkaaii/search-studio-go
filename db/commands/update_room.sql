-- psql -U root -d studio < "/commands/update_room.sql" -v path="'/data/studio - 部屋.csv'"

BEGIN
;

CREATE TEMP TABLE temp_room(
    room_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    room_name VARCHAR,
    reservation_url VARCHAR,
    min_reservable_people INTEGER,
    max_reservable_people INTEGER,
    floor_area FLOAT,
    floor_material_name VARCHAR
)
;

COPY temp_room(studio_name, room_name, reservation_url, min_reservable_people, max_reservable_people, floor_area, floor_material_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

-- スタジオIDを付与する (roomよりも前にstudioが登録されている必要がある)
UPDATE
    temp_room
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_room.studio_name = studio.studio_name
;

INSERT INTO room(
    studio_id,
    room_name,
    reservation_url,
    min_reservable_people,
    max_reservable_people,
    floor_area,
    created_at,
    updated_at,
    is_deleted
)
SELECT DISTINCT
    studio_id,
    room_name,
    reservation_url,
    min_reservable_people,
    max_reservable_people,
    floor_area,
    now(),
    now(),
    false
FROM
    temp_room
ON  CONFLICT(studio_id, room_name) DO
    UPDATE
    SET
        reservation_url = temp_room.reservation_url,
        min_reservable_people = temp_room.min_reservable_people,
        max_reservable_people = temp_room.max_reservable_people,
        floor_area = temp_room.floor_area,
        updated_at = now()
;

INSERT INTO room_floor_material(
    room_id,
    floor_material_id,
    created_at,
    updated_at,
    is_deleted
)
SELECT DISTINCT
    room.room_id,
    floor_material.floor_material_id,
    now(),
    now(),
    false
FROM
    temp_room
        INNER JOIN
    room
    ON  room.studio_id = temp_room.studio_id
        AND room.room_name = temp_room.room_name
        INNER JOIN
    floor_material
    ON  floor_material.floor_material_name = temp_room.floor_material_name
ON  CONFLICT(room_id, floor_material_id) DO NOTHING
;


COMMIT
;
