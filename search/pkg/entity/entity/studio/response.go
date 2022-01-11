package studio

import "time"

type Response struct {
	StudioID int `json:"studio_id"`
	StudioName string `json:"studio_name"`
	Introduction string `json:"introduction"`
	Precaution string `json:"precaution"`
	HomepageURL string `json:"homepage_url"`
	Contact string `json:"contact"`
	Address Address `json:"address"`
	RentByMinHours float64 `json:"rent_by_min_hours"`
	CanFreeCancel bool `json:"can_free_cancel"`
	StudioFacilities []StudioFacility `json:"studio_facilities"`
	StudioAmenities []StudioAmenity `json:"studio_amenities"`
	StudioPayments []StudioPayment `json:"studio_payments"`
	StudioReservations []StudioReservation `json:"studio_reservations"`
	StudioImages []StudioImage `json:"studio_images"`
	StudioAccessByStations []StudioAccessByStation `json:"studio_access_by_stations"`
}
type Address struct {
	AddressID int `json:"address_id"`
	AddressName string `json:"address_name"`
	City City `json:"city"`
}
type City struct {
	CityID int `json:"city_id"`
	CityName string `json:"city_name"`
	Prefecture Prefecture `json:"prefecture"`
}
type Prefecture struct {
	PrefectureID int `json:"prefecture_id"`
	PrefectureName string `json:"prefecture_name"`
}
type StudioFacility struct {
	StudioFacilityID int `json:"studio_facility_id"`
	Facility Facility `json:"facility"`
	StudioFacilityCount int `json:"studio_facility_count"`
	StudioFacilityPrice float64 `json:"studio_facility_price"`
	StudioFacilityUnitHour float64 `json:"studio_facility_unit_hour"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	DeletedAt time.Time `json:"deleted_at"`
	IsDeleted bool `json:"is_deleted"`
}
type Facility struct {
	FacilityID int `json:"facility_id"`
	FacilityName string `json:"facility_name"`
}
type StudioAmenity struct {
	StudioAmenityID int `json:"studio_amenity_id"`
	Amenity Amenity `json:"amenity"`
	StudioAmenityCount int `json:"studio_amenity_count"`
	StudioAmenityPrice float64 `json:"studio_amenity_price"`
	StudioAmenityUnitHour float64 `json:"studio_amenity_unit_hour"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	DeletedAt time.Time `json:"deleted_at"`
	IsDeleted bool `json:"is_deleted"`
}
type Amenity struct {
	AmenityID int `json:"amenity_id"`
	AmenityName string `json:"amenity_name"`
}
type StudioPayment struct {
	StudioPaymentID int `json:"studio_payment_id"`
	Payment Payment `json:"payment"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	DeletedAt time.Time `json:"deleted_at"`
	IsDeleted bool `json:"is_deleted"`
}
type Payment struct {
	PaymentID int `json:"payment_id"`
	PaymentName string `json:"payment_name"`
}
type StudioReservation struct {
	StudioReservationID int `json:"studio_reservation_id"`
	Reservation Reservation `json:"reservation"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	DeletedAt time.Time `json:"deleted_at"`
	IsDeleted bool `json:"is_deleted"`
}
type Reservation struct {
	ReservationID int `json:"reservation_id"`
	ReservationName string `json:"reservation_name"`
}
type StudioImage struct {
	StudioImageID int `json:"studio_image_id"`
	Image Image `json:"image"`
	Description string `json:"description"`
}
type Image struct {
	ImageID int `json:"image_id"`
	ImageName string `json:"image_name"`
	ImagePath string `json:"image_path"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	DeletedAt time.Time `json:"deleted_at"`
	IsDeleted bool `json:"is_deleted"`
}
type StudioAccessByStation struct {
	StudioAccessByStationID int `json:"studio_access_by_station_id"`
	StationRailwayExit StationRailwayExit `json:"station_railway_exit"`
	MinutesFromStation int `json:"minutes_from_station"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	DeletedAt time.Time `json:"deleted_at"`
	IsDeleted bool `json:"is_deleted"`
}
type StationRailwayExit struct {
	StationRailwayExitID int `json:"station_railway_exit_id"`
	StationRailway StationRailway `json:"station_railway"`
	Exit Exit `json:"exit"`
}
type StationRailway struct {
	StationRailwayID int `json:"station_railway_id"`
	Station Station `json:"station"`
	Railway Railway `json:"railway"`
}
type Exit struct {
	ExitID int `json:"exit_id"`
	ExitName string `json:"exit_name"`
}
type Station struct {
	StationID int `json:"station_id"`
	StationName string `json:"station_name"`
}
type Railway struct {
	RailwayID int `json:"railway_id"`
	RailwayName string `json:"railway_name"`
}
