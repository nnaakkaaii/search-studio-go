-- psql -U root -d studio < "/commands/update_amenity_mst.sql" -v path="'/data/studio - アメニティ一覧.csv'"

-- トランザクション開始
BEGIN
;

CREATE TEMP TABLE temp_amenity(
    amenity_id SERIAL PRIMARY KEY,
    amenity_name VARCHAR
)
;

COPY temp_amenity(amenity_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO amenity(
    amenity_name
)
SELECT DISTINCT
    amenity_name
FROM
    temp_amenity
ON  CONFLICT(amenity_name) DO NOTHING
;

COMMIT
;
