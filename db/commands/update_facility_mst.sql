-- psql -U root -d studio < "/commands/update_facility_mst.sql" -v path="'/data/studio - 部屋設備一覧.csv'"
-- psql -U root -d studio < "/commands/update_facility_mst.sql" -v path="'/data/studio - スタジオ設備一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_facility(
    facility_id SERIAL PRIMARY KEY,
    facility_name VARCHAR
)
;

COPY temp_facility(facility_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO facility(
    facility_name
)
SELECT DISTINCT
    facility_name
FROM
    temp_facility
ON  CONFLICT(facility_name) DO NOTHING
;

COMMIT
;
