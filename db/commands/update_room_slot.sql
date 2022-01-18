-- psql -U root -d studio < "/commands/update_room_slot.sql" -v path="'/data/studio - 部屋予約_processed.csv'"

BEGIN
;

CREATE TEMP TABLE temp_room_slot(
    room_slot_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    room_id INTEGER,
    room_name VARCHAR,
    day_template_name VARCHAR,
    workload FLOAT,
    time_begin TIME,
    time_end TIME,
    slot_base_price FLOAT,
    slot_count INTEGER
)
;

COPY temp_room_slot(studio_name, room_name, day_template_name, workload, time_begin, time_end, slot_base_price, slot_count)
    FROM
    :path WITH ENCODING 'utf-8' CSV HEADER
;

UPDATE
    temp_room_slot
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_room_slot.studio_name = studio.studio_name
;

UPDATE
    temp_room_slot
SET
    room_id = room.room_id
FROM
    room
WHERE
    temp_room_slot.studio_id = room.studio_id
    AND temp_room_slot.room_name = room.room_name
;

INSERT INTO day_template(
    day_template_name
)
SELECT DISTINCT
    day_template_name
FROM
    temp_room_slot
ON  CONFLICT(day_template_name) DO NOTHING
;

INSERT INTO room_slot_day_template(
    room_id,
    day_template_id,
    time_begin,
    time_end,
    workload,
    slot_base_price,
    slot_count,
    created_at,
    updated_at,
    is_deleted
)
SELECT
    temp_room_slot.room_id,
    day_template.day_template_id,
    temp_room_slot.time_begin,
    temp_room_slot.time_end,
    temp_room_slot.workload,
    temp_room_slot.slot_base_price,
    temp_room_slot.slot_count,
    now(),
    now(),
    false
FROM
    temp_room_slot
        INNER JOIN
    day_template
        ON day_template.day_template_name = temp_room_slot.day_template_name
ON  CONFLICT(room_id, day_template_id, time_begin, time_end) DO
    UPDATE
    SET
        workload = temp_room_slot.workload,
        slot_base_price = temp_room_slot.slot_base_price,
        slot_count = temp_room_slot.slot_count,
        updated_at = now()
;

COMMIT
;
