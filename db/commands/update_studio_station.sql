-- psql -U root -d studio < "/commands/update_studio_station.sql" -v path="'/data/studio - スタジオ駅.csv'"

BEGIN
;

CREATE TEMP TABLE temp_studio_station(
    studio_station_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    station_id INTEGER,
    station_name VARCHAR,
    railway_id INTEGER,
    railway_name VARCHAR,
    exit_name VARCHAR,
    minutes_from_station INTEGER
)
;

COPY temp_studio_station(studio_name, station_name, railway_name, exit_name, minutes_from_station)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

UPDATE
    temp_studio_station
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_studio_station.studio_name = studio.studio_name
;

DELETE
FROM
    temp_studio_station
WHERE
    studio_id IS NULL
;

UPDATE
    temp_studio_station
SET
    station_id = station.station_id
FROM
    station
WHERE
    temp_studio_station.station_name = station.station_name
;

DELETE
FROM
    temp_studio_station
WHERE
    station_id IS NULL
;

UPDATE
    temp_studio_station
SET
    railway_id = railway.railway_id
FROM
    railway
WHERE
    temp_studio_station.railway_name = railway.railway_name
;

DELETE
FROM
    temp_studio_station
WHERE
    railway_id IS NULL
;

INSERT INTO exit(
    exit_name
)
SELECT DISTINCT
    exit_name
FROM
    temp_studio_station
ON  CONFLICT(exit_name) DO NOTHING
;

INSERT INTO station_railway(
    station_id,
    railway_id
)
SELECT DISTINCT
    station_id,
    railway_id
FROM
    temp_studio_station
ON  CONFLICT(station_id, railway_id) DO NOTHING
;

INSERT INTO station_railway_exit(
    station_railway_id,
    exit_id
)
SELECT DISTINCT
    station_railway.station_railway_id,
    exit.exit_id
FROM
    temp_studio_station
    INNER JOIN
        station_railway
    ON  station_railway.station_id = temp_studio_station.station_id
    AND station_railway.railway_id = temp_studio_station.railway_id
    INNER JOIN
        exit
    ON  exit.exit_name = temp_studio_station.exit_name
ON  CONFLICT(station_railway_id, exit_id) DO NOTHING
;

INSERT INTO studio_station_railway_exit(
    studio_id,
    station_railway_exit_id,
    minutes_from_station,
    created_at,
    is_deleted
)
SELECT DISTINCT
    temp_studio_station.studio_id,
    station_railway_exit.station_railway_exit_id,
    temp_studio_station.minutes_from_station,
    now(),
    false
FROM
    temp_studio_station
    INNER JOIN
        station_railway
    ON  station_railway.station_id = temp_studio_station.station_id
    AND station_railway.railway_id = temp_studio_station.railway_id
    INNER JOIN
        exit
    ON  exit.exit_name = temp_studio_station.exit_name
    INNER JOIN
        station_railway_exit
    ON  station_railway_exit.station_railway_id = station_railway.station_railway_id
    AND station_railway_exit.exit_id = exit.exit_id
ON  CONFLICT(studio_id, station_railway_exit_id) DO NOTHING
;

COMMIT
;
