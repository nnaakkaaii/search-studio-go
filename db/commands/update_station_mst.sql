-- psql -U root -d studio < "/commands/update_station_mst.sql" -v path="'/data/studio - 駅一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_station(
    station_id SERIAL PRIMARY KEY,
    station_name VARCHAR
)
;

COPY temp_station(station_name)
    FROM
    :path WITH ENCODING 'utf_8' CSV
;

INSERT INTO station(
    station_name
)
SELECT DISTINCT
    station_name
FROM
    temp_station
ON  CONFLICT(station_name) DO NOTHING
;

COMMIT
;
