-- psql -U root -d studio < "/commands/update_railway_mst.sql" -v path="'/data/studio - 鉄道一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_railway(
    railway_id SERIAL PRIMARY KEY,
    railway_name VARCHAR
)
;

COPY temp_railway(railway_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO railway(
    railway_name
)
SELECT DISTINCT
    railway_name
FROM
    temp_railway
ON  CONFLICT(railway_name) DO NOTHING
;

COMMIT
;
