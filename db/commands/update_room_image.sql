-- psql -U root -d studio < "/commands/update_room_image.sql" -v path="'/data/studio - 部屋画像.csv'"

BEGIN
;

CREATE TEMP TABLE temp_room_image(
    room_image_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    room_id INTEGER,
    room_name VARCHAR,
    image_path VARCHAR,
    image_name VARCHAR
)
;

COPY temp_room_image(studio_name, room_name, image_path, image_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

-- studio_id
UPDATE
    temp_room_image
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_room_image.studio_name = studio.studio_name
;

-- room_id
UPDATE
    temp_room_image
SET
    room_id = room.room_id
FROM
    room
WHERE
    temp_room_image.studio_id = room.studio_id
    AND temp_room_image.room_name = room.room_name
;

INSERT INTO image(
    image_name,
    image_path,
    created_at,
    updated_at,
    is_deleted
)
SELECT DISTINCT
    image_name,
    image_path,
    now(),
    now(),
    false
FROM
    temp_room_image
ON  CONFLICT(image_name, image_path) DO
    UPDATE
    SET
        updated_at = now()
;

INSERT INTO room_image(
    room_id,
    image_id
)
SELECT DISTINCT
    temp_room_image.room_id,
    image.image_id
FROM
    temp_room_image
        INNER JOIN
    image
    ON  image.image_name = temp_room_image.image_name
        AND image.image_path = temp_room_image.image_path
ON  CONFLICT(room_id, image_id) DO NOTHING
;


COMMIT
;
