-- psql -U root -d studio < "/commands/update_prefecture_mst.sql" -v path="'/data/studio - 都道府県一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_prefecture(
    prefecture_id SERIAL PRIMARY KEY,
    prefecture_name VARCHAR
)
;

COPY temp_prefecture(prefecture_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO prefecture(
    prefecture_name
)
SELECT DISTINCT
    prefecture_name
FROM
    temp_prefecture
ON  CONFLICT(prefecture_name) DO NOTHING
;

COMMIT
;
