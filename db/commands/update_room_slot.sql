-- psql -U root -d studio < "/commands/update_room_slot.sql" -v path="'/data/studio - 部屋予約_processed.csv'"

BEGIN
;

CREATE TEMP TABLE temp_room_slot(
    room_slot_id SERIAL PRIMARY KEY,
    studio_id INTEGER,
    studio_name VARCHAR,
    room_id INTEGER,
    room_name VARCHAR,
    day_template_id INTEGER,
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

-- day_template_id 付与
UPDATE
    temp_room_slot
SET
    day_template_id = day_template.day_template_id
FROM
    day_template
WHERE
    temp_room_slot.day_template_name = day_template.day_template_name
;

DELETE
FROM
    temp_room_slot
WHERE
    day_template_id IS NULL
;

-- studio_id 付与
UPDATE
    temp_room_slot
SET
    studio_id = studio.studio_id
FROM
    studio
WHERE
    temp_room_slot.studio_name = studio.studio_name
;

DELETE
FROM
    temp_room_slot
WHERE
    studio_id IS NULL
;

-- room_id 付与
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

DELETE
FROM
    temp_room_slot
WHERE
    room_id IS NULL
;

-- 重複行確認
SELECT
    *
FROM
    temp_room_slot
WHERE EXISTS(
    SELECT
        room_id,
        day_template_id,
        time_begin
    FROM
        temp_room_slot
    GROUP BY
        room_id,
        day_template_id,
        time_begin
    HAVING
            COUNT(room_id) > 1
       AND COUNT(day_template_id) > 1
       AND COUNT(time_begin) > 1
)
LIMIT
    10
;

SELECT
    *
FROM
    temp_room_slot
WHERE EXISTS(
    SELECT
        room_id,
        day_template_id,
        time_end
    FROM
        temp_room_slot
    GROUP BY
        room_id,
        day_template_id,
        time_end
    HAVING
        COUNT(room_id) > 1
    AND COUNT(day_template_id) > 1
    AND COUNT(time_end) > 1
)
LIMIT
    10
;

-- 代入
INSERT INTO room_slot_day_template(
    room_id,
    day_template_id,
    time_begin,
    time_end,
    workload,
    slot_base_price,
    slot_count,
    created_at,
    is_deleted
)
SELECT
    temp_room_slot.room_id,
    temp_room_slot.day_template_id,
    temp_room_slot.time_begin,
    temp_room_slot.time_end,
    temp_room_slot.workload,
    temp_room_slot.slot_base_price,
    temp_room_slot.slot_count,
    now(),
    false
FROM
    temp_room_slot
ON  CONFLICT(room_id, day_template_id, time_begin) DO
    UPDATE
    SET
        workload = excluded.workload,
        slot_base_price = excluded.slot_base_price,
        slot_count = excluded.slot_count,
        updated_at = now()
;

select * from room_slot_day_template limit 30;

COMMIT
;
