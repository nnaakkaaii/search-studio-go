# graphqlサーバー

## schema

xoを使う場合は、 dockerを立ち上げた状態で

```bash
$ ~/go/bin/xo query 'postgresql://root:postgres@127.0.0.1:5432/studio?sslmode=disable' -M -B -T HogeHoge -o models/ << ENDSQL
...
ENDSQL
```

### studio

```graphql
type Studio {
    studio_id: ID!
    studio_name: String!
    introduction: String
    precaution: String
    homepage_url: String
    contact: String!
    address_id: Int!
    address_name: String!
    city_id: Int!
    city_name: String!
    prefecture_id: Int!
    prefecture_name: String!
    rent_by_min_hours: Float!
    can_free_cancel: Boolean
    studio_facilities: [StudioFacility]  # 紐付けテーブル
    studio_amenities: [StudioAmenity]
    studio_payments: [StudioPayment]
    studio_reservations: [StudioReservation]
    studio_images: [StudioImage]
    studio_station_railway_exits: [StudioStationRailwayExit]
    created_at: DateTime!
    updated_at: DateTime!
}
```

#### StudioByID

```sql
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
```

#### StudiosByName

```sql
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
```


### StudioFacility


```graphql
type StudioFacility {
    studio_facility_id: ID!
    facility_id: Int!
    facility_name: String!
    studio_facility_count: Int
    studio_facility_price: Float
    studio_facility_unit_hour: Float
    created_at: DateTime!
    updated_at: DateTime!
}
```

#### StudioFacilities

```sql
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
```


### StudioAmenity


```graphql
type StudioAmenity {
    studio_amenity_id: ID!
    amenity_id: Int!
    amenity_name: String!
    studio_amenity_count: Int
    studio_amenity_price: Float
    studio_amenity_unit_hour: Float
    created_at: DateTime!
    updated_at: DateTime!
}
```

#### StudioAmenities

```sql
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
```

### StudioPayment

```graphql
type StudioPayment {
    studio_payment_id: ID!
    payment_id: Int!
    payment_name: String!
    created_at: DateTime!
    updated_at: DateTime!
}
```

#### StudioPayments

```sql
SELECT sp.studio_payment_id,
       sp.payment_id,
       p.payment_name,
       sp.created_at,
       sp.updated_at
FROM studio_payment AS sp
    LEFT JOIN payment AS p ON sp.payment_id = p.payment_id
WHERE sp.studio_id = %%studioID int%%
  AND sp.is_deleted IS FALSE;
```

### StudioReservation

```graphql
type StudioReservation {
    studio_reservation_id: ID!
    reservation_id: Int!
    reservation_name: String!
    created_at: DateTime!
    updated_at: DateTime!
}
```

#### StudioReservations

```sql
SELECT sr.studio_reservation_id,
       sr.reservation_id,
       r.reservation_name,
       sr.created_at,
       sr.updated_at
FROM studio_reservation AS sr
    LEFT JOIN reservation AS r ON sr.reservation_id = r.reservation_id
WHERE sr.studio_id = %%studioID int%%
  AND sr.is_deleted IS FALSE;
```

### StudioImage

```graphql
type StudioImage {
    studio_image_id: ID!
    image_id: Int!
    image_name: String!
    image_path: String!
    created_at: DateTime!
    updated_at: DateTime!
    description: String
}
```

#### StudioImages

```sql
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
```


### StudioStationRailwayExit

```graphql
type StudioStationRailwayExit {
    studio_station_railway_exit_id: ID!
    station_railway_exit_id: Int!
    station_railway_id: Int!
    station_id: Int!
    station_name: String!
    railway_id: Int!
    railway_name: String!
    exit_id: ID!
    exit_name: String!
    minutes_from_station: Int
    created_at: DateTime!
    updated_at: DateTime!
}
```

#### StudioStationRailwayExits

```sql
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
```