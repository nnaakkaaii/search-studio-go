-- psql -U root -d studio < "/commands/update_floor_material_mst.sql" -v path="'/data/studio - 部屋床素材一覧.csv'"

BEGIN
;

CREATE TEMP TABLE temp_floor_material(
    floor_material_id SERIAL PRIMARY KEY,
    floor_material_name VARCHAR
)
;

COPY temp_floor_material(floor_material_name)
    FROM
    :path WITH ENCODING 'utf-8' CSV
;

INSERT INTO floor_material(
    floor_material_name
)
SELECT DISTINCT
    floor_material_name
FROM
    temp_floor_material
ON  CONFLICT(floor_material_name) DO NOTHING
;

COMMIT
;
