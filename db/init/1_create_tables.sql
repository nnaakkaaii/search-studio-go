\encoding utf8

DROP DATABASE IF EXISTS tmp;
DROP DATABASE IF EXISTS studio;

CREATE DATABASE studio;

\c studio









-- その他

-- ok
CREATE TABLE image (
    image_id SERIAL PRIMARY KEY,
    image_name VARCHAR(512) NOT NULL,
    image_path VARCHAR(1024) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE(image_name, image_path)
);









-- studioに関する情報

-- ok
CREATE TABLE prefecture (
    prefecture_id SERIAL PRIMARY KEY,
    prefecture_name VARCHAR(256) NOT NULL,
    UNIQUE(prefecture_name)
);

-- ok
CREATE TABLE city (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(256) NOT NULL,
    prefecture_id INTEGER NOT NULL REFERENCES prefecture(prefecture_id) ON DELETE RESTRICT,
    UNIQUE(city_name, prefecture_id)
);

-- ok
CREATE TABLE address (
    address_id SERIAL PRIMARY KEY,
    address_name VARCHAR(1024) NOT NULL,
    city_id INTEGER NOT NULL REFERENCES city(city_id) ON DELETE RESTRICT,
    UNIQUE(address_name)
);

-- ok
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
    is_deleted BOOLEAN NOT NULL,
    UNIQUE(studio_name)
);

-- ok
CREATE TABLE reservation (
    reservation_id SERIAL PRIMARY KEY,
    reservation_name VARCHAR(128) NOT NULL,
    UNIQUE(reservation_name)
);

-- ok
CREATE TABLE studio_reservation (
    studio_reservation_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    reservation_id INTEGER NOT NULL REFERENCES reservation(reservation_id) ON DELETE RESTRICT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, reservation_id)
);

-- ok
CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    payment_name VARCHAR(128) NOT NULL,
    UNIQUE(payment_name)
);

-- ok
CREATE TABLE studio_payment (
    studio_payment_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    payment_id INTEGER NOT NULL REFERENCES payment(payment_id) ON DELETE RESTRICT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, payment_id)
);

-- ok
CREATE TABLE amenity (
    amenity_id SERIAL PRIMARY KEY,
    amenity_name VARCHAR(128) NOT NULL,
    UNIQUE (amenity_name)
);

-- ok
CREATE TABLE studio_amenity (
    studio_amenity_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    amenity_id INTEGER NOT NULL REFERENCES amenity(amenity_id) ON DELETE RESTRICT,
    studio_amenity_serial_number INTEGER NOT NULL,
    studio_amenity_description TEXT,
    studio_amenity_count INTEGER,
    studio_amenity_price FLOAT,
    studio_amenity_unit_hour FLOAT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, amenity_id, studio_amenity_serial_number)
);

-- ok
CREATE TABLE facility (
    facility_id SERIAL PRIMARY KEY,
    facility_name VARCHAR(128) NOT NULL,
    UNIQUE(facility_name)
);

-- ok
CREATE TABLE studio_facility (
    studio_facility_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    facility_id INTEGER NOT NULL REFERENCES facility(facility_id) ON DELETE RESTRICT,
    studio_facility_serial_number INTEGER NOT NULL,
    studio_facility_description TEXT,
    studio_facility_count INTEGER,
    studio_facility_price FLOAT,
    studio_facility_unit_hour FLOAT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, facility_id, studio_facility_serial_number)
);

-- ok
CREATE TABLE studio_image (
   studio_image_id SERIAL PRIMARY KEY,
   studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
   image_id INTEGER NOT NULL REFERENCES image(image_id) ON DELETE RESTRICT,
   description TEXT,
   UNIQUE (studio_id, image_id)
);

-- ok
CREATE TABLE station (
    station_id SERIAL PRIMARY KEY,
    station_name VARCHAR(256) NOT NULL,
    UNIQUE(station_name)
);

-- ok
CREATE TABLE railway (
    railway_id SERIAL PRIMARY KEY,
    railway_name VARCHAR(128),
    UNIQUE(railway_name)
);

-- ok
CREATE TABLE station_railway (
    station_railway_id SERIAL PRIMARY KEY,
    station_id INTEGER NOT NULL REFERENCES station(station_id) ON DELETE RESTRICT,
    railway_id INTEGER NOT NULL REFERENCES railway(railway_id) ON DELETE RESTRICT,
    UNIQUE (station_id, railway_id)
);

CREATE TABLE line (
    line_id SERIAL PRIMARY KEY,
    line_name VARCHAR(256) NOT NULL,
    UNIQUE(line_name)
);

CREATE TABLE station_railway_line (
    station_railway_line_id SERIAL PRIMARY KEY,
    station_railway_id INTEGER NOT NULL REFERENCES station_railway(station_railway_id) ON DELETE RESTRICT,
    line_id INTEGER NOT NULL REFERENCES line(line_id) ON DELETE RESTRICT,
    UNIQUE (station_railway_id, line_id)
);

-- ok
CREATE TABLE exit (
    exit_id SERIAL PRIMARY KEY,
    exit_name VARCHAR(128) NOT NULL,
    UNIQUE(exit_name)
);

-- ok
CREATE TABLE station_railway_exit (
    station_railway_exit_id SERIAL PRIMARY KEY,
    station_railway_id INTEGER NOT NULL REFERENCES station_railway(station_railway_id) ON DELETE RESTRICT,
    exit_id INTEGER NOT NULL REFERENCES exit(exit_id) ON DELETE RESTRICT,
    UNIQUE (station_railway_id, exit_id)
);

CREATE TABLE studio_station_railway_exit (
    studio_station_railway_exit_id SERIAL PRIMARY KEY,
    studio_id INTEGER NOT NULL REFERENCES studio(studio_id) ON DELETE RESTRICT,
    station_railway_exit_id INTEGER NOT NULL REFERENCES station_railway_exit(station_railway_exit_id) ON DELETE RESTRICT,
    minutes_from_station INTEGER,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (studio_id, station_railway_exit_id)
);









-- roomに関する情報

-- ok
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
    is_deleted BOOLEAN NOT NULL,
    UNIQUE(studio_id, room_name)
);

-- ok
CREATE TABLE floor_material (
    floor_material_id SERIAL PRIMARY KEY,
    floor_material_name VARCHAR(128) NOT NULL,
    UNIQUE(floor_material_name)
);

-- ok
CREATE TABLE room_floor_material (
    room_floor_material_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    floor_material_id INTEGER NOT NULL REFERENCES floor_material(floor_material_id) ON DELETE RESTRICT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (room_id, floor_material_id)
);

-- ok
CREATE TABLE room_facility (
    room_facility_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    facility_id INTEGER NOT NULL REFERENCES facility(facility_id) ON DELETE RESTRICT,
    room_facility_serial_number INTEGER NOT NULL,
    room_facility_description TEXT,
    room_facility_count INTEGER,
    room_facility_price FLOAT,
    room_facility_unit_hour FLOAT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (room_id, facility_id, room_facility_serial_number)
);

-- ok
CREATE TABLE room_image (
    room_image_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    image_id INTEGER NOT NULL REFERENCES image(image_id) ON DELETE RESTRICT,
    description TEXT,
    UNIQUE (room_id, image_id)
);









-- slotに関する情報

CREATE TABLE day_template (
    day_template_id SERIAL PRIMARY KEY,
    day_template_name VARCHAR(128) NOT NULL,
    UNIQUE(day_template_name)
);

CREATE TABLE room_slot_day_template (
    room_slot_day_template_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    day_template_id INTEGER NOT NULL REFERENCES day_template(day_template_id) ON DELETE RESTRICT,
    time_begin TIME NOT NULL,
    time_end TIME NOT NULL,
    workload FLOAT NOT NULL,
    slot_base_price FLOAT NOT NULL,
    slot_count INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (room_id, day_template_id, time_begin),
    UNIQUE (room_id, day_template_id, time_end)
);

CREATE TABLE room_slot (
    room_slot_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES room(room_id) ON DELETE RESTRICT,
    date DATE NOT NULL,
    time_begin TIME NOT NULL,
    time_end TIME NOT NULL,
    workload FLOAT NOT NULL,
    slot_price INTEGER NOT NULL,
    remain_slot_count INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP,
    is_deleted BOOLEAN NOT NULL,
    UNIQUE (room_id, date, time_begin),
    UNIQUE (room_id, date, time_end)
);









CREATE DATABASE tmp;
