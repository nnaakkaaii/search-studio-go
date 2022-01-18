-- psql -U root -d studio < "/commands/update_city_mst.sql" -v path="'/data/studio - 市区町村一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_city(
    city_id SERIAL PRIMARY KEY,
    prefecture_name VARCHAR,
    city_name VARCHAR
)
;

COPY temp_city(prefecture_name, city_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO city(
    city_name,
    prefecture_id
)
SELECT DISTINCT
    temp_city.city_name,
    prefecture.prefecture_id
FROM
    temp_city
        INNER JOIN
    prefecture
    ON  prefecture.prefecture_name = temp_city.prefecture_name
ON  CONFLICT(city_name) DO NOTHING
;

COMMIT
;
