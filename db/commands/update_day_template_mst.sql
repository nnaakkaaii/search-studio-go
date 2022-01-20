-- psql -U root -d studio < "/commands/update_day_template_mst.sql" -v path="'/data/studio - 曜日一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_day_template(
    day_template_id INTEGER PRIMARY KEY,
    day_template_name VARCHAR
)
;

COPY temp_day_template(day_template_id, day_template_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO day_template(
    day_template_id,
    day_template_name
)
SELECT DISTINCT
    day_template_id,
    day_template_name
FROM
    temp_day_template
ON  CONFLICT(day_template_id) DO
    UPDATE
    SET
        day_template_name = excluded.day_template_name
;

COMMIT
;
