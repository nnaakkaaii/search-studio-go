~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T StudioByID -o models/ << ENDSQL
SELECT s.studio_id,
       s.studio_name,
       s.introduction,
       s.precaution,
       s.homepage_url,
       s.contact,
       a.address_id,
       a.address_name,
       c.city_id,
       c.city_name,
       p.prefecture_id,
       p.prefecture_name,
       s.rent_by_min_hours,
       s.can_free_cancel,
       s.created_at,
       s.updated_at
FROM studio AS s
    LEFT JOIN address AS a ON s.address_id = a.address_id
    LEFT JOIN city AS c ON a.city_id = c.city_id
    LEFT JOIN prefecture AS p ON p.prefecture_id = c.prefecture_id
WHERE s.studio_id = %%studioID int%%
  AND s.is_deleted IS FALSE;
ENDSQL

~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T StudiosByName -o models/ <<ENDSQL
SELECT s.studio_id,
       s.studio_name,
       s.introduction,
       s.precaution,
       s.homepage_url,
       s.contact,
       a.address_id,
       a.address_name,
       c.city_id,
       c.city_name,
       p.prefecture_id,
       p.prefecture_name,
       s.rent_by_min_hours,
       s.can_free_cancel,
       s.created_at,
       s.updated_at
FROM studio AS s
    LEFT JOIN address AS a ON s.address_id = a.address_id
    LEFT JOIN city AS c ON a.city_id = c.city_id
    LEFT JOIN prefecture AS p ON p.prefecture_id = c.prefecture_id
WHERE s.studio_name = %%studioName string%%
  AND s.is_deleted IS FALSE;
ENDSQL

~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T StudioFacilities -o models/ <<ENDSQL
SELECT sf.studio_facility_id,
       sf.facility_id,
       f.facility_name,
       sf.studio_facility_count,
       sf.studio_facility_price,
       sf.studio_facility_unit_hour,
       sf.created_at,
       sf.updated_at
FROM studio_facility AS sf
    LEFT JOIN facility AS f ON sf.facility_id = f.facility_id
WHERE sf.studio_id = %%studioID int%%
  AND sf.is_deleted IS FALSE;
ENDSQL

~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T StudioAmenities -o models/ <<ENDSQL
SELECT sa.studio_amenity_id,
       sa.amenity_id,
       a.amenity_name,
       sa.studio_amenity_count,
       sa.studio_amenity_price,
       sa.studio_amenity_unit_hour,
       sa.created_at,
       sa.updated_at
FROM studio_amenity AS sa
    LEFT JOIN amenity AS a ON sa.amenity_id = a.amenity_id
WHERE sa.studio_id = %%studioID int%%
  AND sa.is_deleted IS FALSE;
ENDSQL

~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T StudioPayments -o models/ <<ENDSQL
SELECT sp.studio_payment_id,
       sp.payment_id,
       p.payment_name,
       sp.created_at,
       sp.updated_at
FROM studio_payment AS sp
    LEFT JOIN payment AS p ON sp.payment_id = p.payment_id
WHERE sp.studio_id = %%studioID int%%
  AND sp.is_deleted IS FALSE;
ENDSQL

~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T StudioReservations -o models/ <<ENDSQL
SELECT sr.studio_reservation_id,
       sr.reservation_id,
       r.reservation_name,
       sr.created_at,
       sr.updated_at
FROM studio_reservation AS sr
    LEFT JOIN reservation AS r ON sr.reservation_id = r.reservation_id
WHERE sr.studio_id = %%studioID int%%
  AND sr.is_deleted IS FALSE;
ENDSQL

~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T StudioImages -o models/ <<ENDSQL
SELECT si.studio_image_id,
       si.image_id,
       i.image_name,
       i.image_path,
       i.created_at,
       i.updated_at,
       si.description
FROM studio_image AS si
    LEFT JOIN Image AS i ON si.image_id = i.image_id
WHERE si.studio_id = %%studioID int%%
  AND i.is_deleted IS FALSE;
ENDSQL

~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T StudioStationRailwayExits -o models/ <<ENDSQL
SELECT ssre.studio_station_railway_exit_id,
       ssre.station_railway_exit_id,
       sre.station_railway_id,
       sr.station_id,
       s.station_name,
       sr.railway_id,
       r.railway_name,
       sre.exit_id,
       e.exit_name,
       ssre.minutes_from_station,
       ssre.created_at,
       ssre.updated_at
FROM studio_station_railway_exit AS ssre
    LEFT JOIN station_railway_exit AS sre ON ssre.station_railway_exit_id = sre.station_railway_exit_id
    LEFT JOIN station_railway AS sr ON sre.station_railway_id = sr.station_railway_id
    LEFT JOIN station AS s ON sr.station_id = s.station_id
    LEFT JOIN railway AS r ON sr.railway_id = r.railway_id
    LEFT JOIN exit AS e ON sre.exit_id = e.exit_id
WHERE ssre.studio_id = %%studioID int%%
  AND ssre.is_deleted IS FALSE;
ENDSQL

python3 ./preprocess/preprocess_xo.py