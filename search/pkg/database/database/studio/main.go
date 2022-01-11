package studio

import (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"
	studio2 "search/pkg/entity/entity/studio"
	"search/pkg/repository/database_interface/studio"
)

type Database struct {
	handler *sql.DB
}

type DatabaseInput struct {
	DBUser string
	DBPass string
	DBHost string
	DBPort string
	DBName string
}

var _ studio.DatabaseInterface = (*Database)(nil)

func NewDatabase(i *DatabaseInput) *Database {
	ds := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable", i.DBHost, i.DBPort, i.DBUser, i.DBPass, i.DBName)
	connector, err := sql.Open("postgres", ds)
	if err != nil {
		panic(err.Error())
	}
	return &Database{handler: connector}
}

func (d *Database) Read(q studio2.Query) (studio2.Response, error) {
	query := `
		SELECT row_to_json(st)
		FROM (
			SELECT studio_id, studio_name, introduction, precaution, homepage_url, contact, (
		    	SELECT row_to_json(ad)
		        FROM (
		            SELECT address_id, address_name, (
		                SELECT row_to_json(ci)
		                FROM (
		                    SELECT city_id, city_name, (
		                        SELECT row_to_json(pr)
		                        FROM (
		                        	SELECT prefecture_id, prefecture_name
		                            FROM prefecture
		                            WHERE prefecture.prefecture_id = city.prefecture_id
		                        ) pr
		                    ) as prefecture
		                    FROM city
		                    WHERE city.city_id = adress.address_id
		                ) ci
		            ) as city
		            FROM address
		            WHERE address.address_id = studio.address_id
		        ) ad
		    ) as address, rent_by_min_hours, can_free_cancel, (
		        SELECT array_to_json(array_agg(sf))
		        FROM (
		            SELECT studio_facility_id, (
		                SELECT row_to_json(fc)
		                FROM (
		                    SELECT facility_id, facility_name
		                    FROM facility
		                    WHERE facility.facility_id = studio_facility.facility_id
		                ) fc
		            ) as facility, studio_facility_count, studio_facility_price, studio_facility_unit_hour, created_at, updated_at, deleted_at, is_deleted
		            FROM studio_facility
		            WHERE studio_facility.studio_id = studio.studio_id
		        ) sf
		    ) as studio_facilities, (
		        SELECT array_to_json(array_agg(sa))
		        FROM (
		            SELECT studio_amenity_id, (
		                SELECT row_to_json(am)
		                FROM (
		                    SELECT amenity_id, amenity_name
		                    FROM amenity
		                    WHERE amenity.amenity_id = studio_amenity.amenity_id
		                ) am
		            ) as amenity, studio_amenity_count, studio_amenity_price, studio_amenity_unit_hour, created_at, updated_at, deleted_at, is_deleted
		        	FROM studio_amenity
		            WHERE studio_amenity.studio_id = studio.studio_id
		        ) sa
		    ) as studio_amenities, (
		        SELECT array_to_json(array_agg(sp))
		        FROM (
		            SELECT studio_payment_id, (
		            	SELECT row_to_json(pa)
		                FROM (
		                    SELECT payment_id, payment_name
		                    FROM payment
		                    WHERE payment.payment_id = studio_payment.payment_id
		                ) pa
		            ) as payment, created_at, updated_at, deleted_at, is_deleted
		            FROM studio_payment
		            WHERE studio_payment.studio_id = studio.studio_id
		        ) sp
		    ) as studio_payments, (
		        SELECT array_to_json(array_agg(sr))
		        FROM (
		            SELECT studio_reservation_id, (
		            	SELECT row_to_json(re)
		                FROM (
		                    SELECT reservation_id, reservation_name
		                    FROM reservation
		                    WHERE reservation.reservation_id = studio_reservation.reservation_id
		                ) re
		            ) as reservation, created_at, updated_at, deleted_at, is_deleted
		            FROM studio_reservation
		            WHERE studio_reservation.studio_id = studio.studio_id
		        ) sr
		    ) as studio_reservations, (
		        SELECT array_to_json(array_agg(si))
		        FROM (
		            SELECT studio_image_id, (
		                SELECT row_to_json(im)
		                FROM (
		                    SELECT image_id, image_name, image_path, created_at, updated_at, deleted_at, is_deleted
		                    FROM image
		                    WHERE image.image_id = studio_image.image_id
		                ) im
		            ) as image, description
		            FROM studio_image
		            WHERE studio_image.studio_id = studio.studio_id
		        ) si
		    ) as studio_images, (
		        SELECT array_to_json(array_agg(sabs))
		        FROM (
		            SELECT studio_access_by_station_id, (
		                SELECT row_to_json(sre)
		                FROM (
		                    SELECT station_railway_exit_id, (
		                        SELECT row_to_json(sr)
		                        FROM (
		                            SELECT station_railway_id, (
		                                SELECT row_to_json(st)
		                                FROM (
		                                    SELECT station_id, station_name
		                                    FROM station
		                                    WHERE station.station_id = station_railway_id.station_id
		                                ) st
		                            ) as station, (
		                                SELECT row_to_json(ra)
		                                FROM (
		                                    SELECT railway_id, railway_name
		                                    FROM railway
		                                    WHERE railway.railway_id = station_railway_id.railway_id
		                                ) ra
		                            ) as railway
		                            FROM station_railway
		                            WHERE station_railway.station_railway_id = station_railway_exit.station_railway_id
		                        ) sr
		                    ) as station_railway, (
		                        SELECT row_to_json(ex)
		                        FROM (
		                            SELECT exit_id, exit_name
		                            FROM exit
		                            WHERE exit.exit_id = station_railway_exit.exit_id
		                        ) ex
		                    ) as exit
		                    FROM station_railway_exit
		                    WHERE station_railway_exit.station_railway_exit_id = studio_access_by_station.station_railway_exit_id
		                ) sre
		            ) as station_railway_exit, minutes_from_station, created_at, updated_at, deleted_at, is_deleted
		            FROM studio_access_by_station
		            WHERE studio_access_by_station.studio_id = studio.studio_id
		        ) sabs
		    )
		    FROM studio
		    WHERE studio.studio_id = %d
		) st;
	`
	rows, err := d.handler.Query(query)
}
