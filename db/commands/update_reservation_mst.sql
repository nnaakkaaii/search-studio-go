-- psql -U root -d studio < "/commands/update_reservation_mst.sql" -v path="'/data/studio - 予約方法一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_reservation(
    reservation_id SERIAL PRIMARY KEY,
    reservation_name VARCHAR
)
;

COPY temp_reservation(reservation_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO reservation(
    reservation_name
)
SELECT DISTINCT
    reservation_name
FROM
    temp_reservation
ON  CONFLICT(reservation_name) DO NOTHING
;

COMMIT
;
