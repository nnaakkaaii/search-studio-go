-- psql -U root -d studio < "/commands/update_studio.sql" -v path="'/data/studio - スタジオ.csv'"

BEGIN
;

CREATE TEMP TABLE temp_studio (
    studio_id SERIAL PRIMARY KEY,
    studio_name VARCHAR,
    homepage_url VARCHAR,
    contact VARCHAR,
    address_name VARCHAR,
    prefecture_id INTEGER,
    prefecture_name VARCHAR,
    city_id INTEGER,
    city_name VARCHAR,
    rent_by_min_hours FLOAT,
    can_free_cancel BOOLEAN
);

COPY temp_studio(studio_name, homepage_url, contact, address_name, prefecture_name, city_name, rent_by_min_hours, can_free_cancel)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

-- prefecture_id
UPDATE
    temp_studio
SET
    prefecture_id = prefecture.prefecture_id
FROM
    prefecture
WHERE
    temp_studio.prefecture_name = prefecture.prefecture_name
;

-- city_id
UPDATE
    temp_studio
SET
    city_id = city.city_id
FROM
    city
WHERE
    temp_studio.prefecture_id = city.prefecture_id
    AND temp_studio.city_name = city.city_name
;

INSERT INTO address(
    address_name,
    city_id
)
SELECT DISTINCT
    address_name,
    city_id
FROM
    temp_studio
ON  CONFLICT(address_name) DO
    UPDATE
    SET
        city_id = temp_studio.city_id
;

INSERT INTO studio(
    studio_name,
    homepage_url,
    contact,
    address_id,
    rent_by_min_hours,
    can_free_cancel,
    created_at,
    updated_at,
    is_deleted
)
SELECT DISTINCT
    temp_studio.studio_name,
    temp_studio.homepage_url,
    temp_studio.contact,
    address.address_id,
    temp_studio.rent_by_min_hours,
    temp_studio.can_free_cancel,
    now(),
    now(),
    false
FROM
    temp_studio
        INNER JOIN
    address
    ON  address.address_name = temp_studio.address_name
ON  CONFLICT(studio_name) DO
    UPDATE
    SET
        homepage_url = temp_studio.homepage_url,
        contact = temp_studio.contact,
        address_id = address.address_id,
        rent_by_min_hours = temp_studio.rent_by_min_hours,
        can_free_cancel = temp_studio.can_free_cancel
;

COMMIT
;
