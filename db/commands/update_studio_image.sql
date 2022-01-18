-- psql -U root -d studio < "/commands/update_studio_image.sql" -v path="'/data/studio - スタジオ画像.csv'"

BEGIN
;

CREATE TEMP TABLE temp_studio_image(
    studio_image_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    image_path VARCHAR,
    image_name VARCHAR
)
;

COPY temp_studio_image(studio_name, image_path, image_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

UPDATE
    temp_studio_image
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_studio_image.studio_name = studio.studio_name
;

INSERT INTO image(
    image_name,
    image_path,
    created_at,
    updated_at,
    is_deleted
)
SELECT
    image_name,
    image_path,
    now(),
    now(),
    false
FROM
    temp_studio_image
ON  CONFLICT(image_name, image_path) DO
    UPDATE
    SET
        updated_at = now()
;

INSERT INTO studio_image(
    studio_id,
    image_id
)
SELECT DISTINCT
    temp_studio_image.studio_id,
    image.image_id
FROM
    temp_studio_image
        INNER JOIN
    image
    ON  image.image_name = temp_studio_image.image_name
        AND image.image_path = temp_studio_image.image_path
ON  CONFLICT(studio_id, image_id) DO NOTHING
;

COMMIT
;
