\encoding utf8

DROP DATABASE IF EXISTS tmp;
DROP DATABASE IF EXISTS studio;

CREATE DATABASE studio;

\c studio









-- その他

CREATE TABLE image (
    image_id SERIAL PRIMARY KEY,
    image_name VARCHAR(512) NOT NULL,
    image_path VARCHAR(1024) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL
);









-- studioに関する情報

CREATE TABLE prefecture (
    prefecture_id SERIAL PRIMARY KEY,
    prefecture_name VARCHAR(256) NOT NULL
);

CREATE TABLE city (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(256) NOT NULL,
    prefecture_id INTEGER NOT NULL REFERENCES prefecture(prefecture_id) ON DELETE RESTRICT
);

CREATE TABLE address (
    address_id SERIAL PRIMARY KEY,
    address_name VARCHAR(1024) NOT NULL,
    city_id INTEGER NOT NULL REFERENCES city(city_id) ON DELETE RESTRICT
);

CREATE TABLE studio (
    studio_id SERIAL PRIMARY KEY,
    studio_name VARCHAR(1024) NOT NULL,
    introduction TEXT,
    precaution TEXT,
    homepage_url VARCHAR(1024),
    contact VARCHAR(11) NOT NULL,
    address_id INTEGER NOT NULL REFERENCES address(address_id) ON DELETE RESTRICT,
    rent_by_min_hours FLOAT NOT NULL,
    can_free_cancel BOOLEAN,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL
);

CREATE TABLE reservation (
    reservation_id SERIAL PRIMARY KEY,
    reservation_name VARCHAR(128) NOT NULL
);

CREATE TABLE studio_reservation_link (
    studio_reservation_link_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    reservation_id INTEGER NOT NULL REFERENCES reservation(reservation_id) ON DELETE RESTRICT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, reservation_id)
);

CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    payment_name VARCHAR(128) NOT NULL
);

CREATE TABLE studio_payment_link (
    studio_payment_link_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    payment_id INTEGER NOT NULL REFERENCES payment(payment_id) ON DELETE RESTRICT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, payment_id)
);

CREATE TABLE amenity (
    amenity_id SERIAL PRIMARY KEY,
    amenity_name VARCHAR(128) NOT NULL
);

CREATE TABLE studio_amenity_link (
    studio_amenity_link_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    amenity_id INTEGER NOT NULL REFERENCES amenity(amenity_id) ON DELETE RESTRICT,
    studio_amenity_count INTEGER,
    studio_amenity_price FLOAT,
    studio_amenity_unit_hour FLOAT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, amenity_id)
);

CREATE TABLE facility (
    facility_id SERIAL PRIMARY KEY,
    facility_name VARCHAR(128) NOT NULL
);

CREATE TABLE studio_facility_link (
    studio_facility_link_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    facility_id INTEGER NOT NULL REFERENCES facility(facility_id) ON DELETE RESTRICT,
    studio_facility_count INTEGER,
    studio_facility_price FLOAT,
    studio_facility_unit_hour FLOAT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, facility_id)
);

CREATE TABLE studio_image_link (
   studio_image_link_id SERIAL PRIMARY KEY,
   studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
   image_id INTEGER NOT NULL REFERENCES image(image_id) ON DELETE RESTRICT,
   description TEXT,
   UNIQUE (studio_id, image_id)
);

CREATE TABLE station (
    station_id SERIAL PRIMARY KEY,
    station_name VARCHAR(256) NOT NULL
);

CREATE TABLE railway (
    railway_id SERIAL PRIMARY KEY,
    railway_name VARCHAR(128)
);

CREATE TABLE station_railway_link (
    station_railway_link_id SERIAL PRIMARY KEY,
    station_id INTEGER NOT NULL REFERENCES station(station_id) ON DELETE RESTRICT,
    railway_id INTEGER NOT NULL REFERENCES railway(railway_id) ON DELETE RESTRICT,
    UNIQUE (station_id, railway_id)
);

CREATE TABLE line (
    line_id SERIAL PRIMARY KEY,
    line_name VARCHAR(256) NOT NULL
);

CREATE TABLE station_railway_line_link (
    station_railway_line_link_id SERIAL PRIMARY KEY,
    station_railway_link_id INTEGER NOT NULL REFERENCES station_railway_link(station_railway_link_id) ON DELETE RESTRICT,
    line_id INTEGER NOT NULL REFERENCES line(line_id) ON DELETE RESTRICT,
    UNIQUE (station_railway_link_id, line_id)
);

CREATE TABLE exit (
    exit_id SERIAL PRIMARY KEY,
    exit_name VARCHAR(128) NOT NULL
);

CREATE TABLE station_railway_exit_link (
    station_railway_exit_link_id SERIAL PRIMARY KEY,
    station_railway_link_id INTEGER NOT NULL REFERENCES station_railway_link(station_railway_link_id) ON DELETE RESTRICT,
    exit_id INTEGER NOT NULL REFERENCES exit(exit_id) ON DELETE RESTRICT,
    UNIQUE (station_railway_link_id, exit_id)
);

CREATE TABLE studio_access_by_station_link (
    studio_access_by_station_link_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    station_railway_exit_link_id INTEGER NOT NULL REFERENCES station_railway_exit_link(station_railway_exit_link_id) ON DELETE RESTRICT,
    minutes_from_station INTEGER,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, station_railway_exit_link_id)
);









-- roomに関する情報

CREATE TABLE room (
    room_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    room_name VARCHAR(512) NOT NULL,
    reservation_url VARCHAR(1024),
    min_reservable_people INTEGER,
    max_reservable_people INTEGER,
    floor_area FLOAT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL
);

CREATE TABLE floor_material (
    floor_material_id SERIAL PRIMARY KEY,
    floor_material_name VARCHAR(128) NOT NULL
);

CREATE TABLE room_floor_material_link (
    room_floor_material_link_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    floor_material_id INTEGER NOT NULL REFERENCES floor_material(floor_material_id) ON DELETE RESTRICT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (room_id, floor_material_id)
);

CREATE TABLE room_facility_link (
    room_facility_link_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    facility_id INTEGER NOT NULL REFERENCES facility(facility_id) ON DELETE RESTRICT,
    room_facility_count INTEGER,
    room_facility_price FLOAT,
    room_facility_unit_hour FLOAT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (room_id, facility_id)
);

CREATE TABLE room_image_link (
    room_image_link_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    image_id INTEGER NOT NULL REFERENCES image(image_id) ON DELETE RESTRICT,
    description TEXT,
    UNIQUE (room_id, image_id)
);









-- slotに関する情報

CREATE TABLE slot (
    slot_id SERIAL PRIMARY KEY,
    workload FLOAT NOT NULL,
    time_begin TIME NOT NULL,
    time_end TIME NOT NULL,
    slot_base_price FLOAT NOT NULL,
    slot_count INTEGER NOT NULL
);

CREATE TABLE day_template (
    day_template_id SERIAL PRIMARY KEY,
    day_template_name VARCHAR(128) NOT NULL
);

CREATE TABLE slot_day_template_link (
    slot_day_template_link_id SERIAL PRIMARY KEY,
    slot_id INTEGER NOT NULL REFERENCES slot(slot_id) ON DELETE RESTRICT,
    day_template_id INTEGER NOT NULL REFERENCES day_template(day_template_id) ON DELETE RESTRICT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (slot_id, day_template_id)
);

CREATE TABLE date_slot_link (
    date_slot_link_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    slot_id INTEGER NOT NULL REFERENCES slot(slot_id) ON DELETE RESTRICT,
    UNIQUE (date, slot_id)
);

CREATE TABLE room_slot_link (
    room_slot_link_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    date_slot_link_id INTEGER NOT NULL REFERENCES date_slot_link(date_slot_link_id) ON DELETE RESTRICT,
    remain_slot_count INTEGER NOT NULL,
    slot_price INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (room_id, date_slot_link_id)
);









CREATE DATABASE tmp;
