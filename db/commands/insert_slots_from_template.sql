BEGIN
;


-- キーとしての一意性の観点から、1週間ずつのinsertになる
CREATE TEMP TABLE temp_schedule AS
SELECT
    d AS date,
    date_part(
        'dow',
        d
    ) AS day_template_id
FROM
    generate_series(
        current_date,
        current_date + interval '6 days',
        interval '1 days'
    ) d
;

select * from temp_schedule;
select * from room_slot_day_template limit 30;

INSERT INTO room_slot(
    room_id,
    date,
    time_begin,
    time_end,
    workload,
    slot_price,
    remain_slot_count,
    created_at,
    is_deleted
)
SELECT DISTINCT
    room_slot_day_template.room_id,
    temp_schedule.date,
    room_slot_day_template.time_begin,
    room_slot_day_template.time_end,
    room_slot_day_template.workload,
    room_slot_day_template.slot_base_price,
    room_slot_day_template.slot_count,
    now(),
    false
FROM
    room_slot_day_template
    INNER JOIN
        temp_schedule
    ON  temp_schedule.day_template_id = room_slot_day_template.day_template_id
ON  CONFLICT(room_id, date, time_begin) DO
    UPDATE
    SET
        workload = excluded.workload,
        slot_price = excluded.slot_price,
        remain_slot_count = excluded.remain_slot_count,
        updated_at = now()
;


COMMIT
;
