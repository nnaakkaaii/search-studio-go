from django_filters import rest_framework as filters

from crud import models

# modelのfieldがCharField,TextFieldの場合
CHAR_FILTER_LIST = [
    'exact',
    'in',
    'contains',
    'startswith',
    'endswith',
    'regex',
    'in',
    'isnull',
]

# modelのfieldがIntegerField, FloatField, DecimalFieldの場合
NUMBER_FILTER_LIST = [
    'exact',
    'in',
    'gt',
    'lt',
    'gte',
    'lte',
    'isnull',
]

# modelのfieldがDataTimeFieldの場合
DATETIME_FILTER_LIST = [
    'exact',
    'in',
    'date',
    'year',
    'month',
    'day',
    'week_day',
    'hour',
    'minute',
    'second',
    'gt',
    'lt',
    'gte',
    'lte',
    'isnull',
]

# modelのfieldがDateFieldの場合
DATE_FILTER_LIST = [
    'exact',
    'in',
    'year',
    'month',
    'day',
    'week_day',
    'gt',
    'lt',
    'gte',
    'lte',
    'isnull',
]

# modelのfieldがTimeFieldの場合
TIME_FILTER_LIST = [
    'exact',
    'in',
    'hour',
    'minute',
    'second',
    'gt',
    'lt',
    'gte',
    'lte',
    'isnull',
]

# modelのfieldがBooleanFieldの場合
BOOLEAN_FILTER_LIST = [
    'isnull',
]


class AddressFilter(filters.FilterSet):
    class Meta:
        model = models.Address
        fields = {
            'address_id': NUMBER_FILTER_LIST,
            'address_name': CHAR_FILTER_LIST,
            'city': NUMBER_FILTER_LIST,
        }


class AmenityFilter(filters.FilterSet):
    class Meta:
        model = models.Amenity
        fields = {
            'amenity_id': NUMBER_FILTER_LIST,
            'amenity_name': CHAR_FILTER_LIST,
        }


class CityFilter(filters.FilterSet):
    class Meta:
        model = models.City
        fields = {
            'city_id': NUMBER_FILTER_LIST,
            'city_name': CHAR_FILTER_LIST,
            'prefecture': NUMBER_FILTER_LIST,
        }


class DayTemplateFilter(filters.FilterSet):
    class Meta:
        model = models.DayTemplate
        fields = {
            'day_template_id': NUMBER_FILTER_LIST,
            'day_template_name': CHAR_FILTER_LIST,
        }


class ExitFilter(filters.FilterSet):
    class Meta:
        model = models.Exit
        fields = {
            'exit_id': NUMBER_FILTER_LIST,
            'exit_name': CHAR_FILTER_LIST,
        }


class FacilityFilter(filters.FilterSet):
    class Meta:
        model = models.Facility
        fields = {
            'facility_id': NUMBER_FILTER_LIST,
            'facility_name': CHAR_FILTER_LIST,
        }


class FloorMaterialFilter(filters.FilterSet):
    class Meta:
        model = models.FloorMaterial
        fields = {
            'floor_material_id': NUMBER_FILTER_LIST,
            'floor_material_name': CHAR_FILTER_LIST,
        }


class ImageFilter(filters.FilterSet):
    class Meta:
        model = models.Image
        fields = {
            'image_id': NUMBER_FILTER_LIST,
            'image_name': CHAR_FILTER_LIST,
            'image_path': CHAR_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class LineFilter(filters.FilterSet):
    class Meta:
        model = models.Line
        fields = {
            'line_id': NUMBER_FILTER_LIST,
            'line_name': CHAR_FILTER_LIST,
        }


class PaymentFilter(filters.FilterSet):
    class Meta:
        model = models.Payment
        fields = {
            'payment_id': NUMBER_FILTER_LIST,
            'payment_name': CHAR_FILTER_LIST,
        }


class PrefectureFilter(filters.FilterSet):
    class Meta:
        model = models.Prefecture
        fields = {
            'prefecture_id': NUMBER_FILTER_LIST,
            'prefecture_name': CHAR_FILTER_LIST,
        }


class RailwayFilter(filters.FilterSet):
    class Meta:
        model = models.Railway
        fields = {
            'railway_id': NUMBER_FILTER_LIST,
            'railway_name': CHAR_FILTER_LIST,
        }


class ReservationFilter(filters.FilterSet):
    class Meta:
        model = models.Reservation
        fields = {
            'reservation_id': NUMBER_FILTER_LIST,
            'reservation_name': CHAR_FILTER_LIST,
        }


class RoomFilter(filters.FilterSet):
    class Meta:
        model = models.Room
        fields = {
            'room_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'room_name': CHAR_FILTER_LIST,
            'reservation_url': CHAR_FILTER_LIST,
            'min_reservable_people': NUMBER_FILTER_LIST,
            'max_reservable_people': NUMBER_FILTER_LIST,
            'floor_area': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class RoomFacilityFilter(filters.FilterSet):
    class Meta:
        model = models.RoomFacility
        fields = {
            'room_facility_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'facility': NUMBER_FILTER_LIST,
            'room_facility_serial_number': NUMBER_FILTER_LIST,
            'room_facility_description': CHAR_FILTER_LIST,
            'room_facility_count': NUMBER_FILTER_LIST,
            'room_facility_price': NUMBER_FILTER_LIST,
            'room_facility_unit_hour': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class RoomFloorMaterialFilter(filters.FilterSet):
    class Meta:
        model = models.RoomFloorMaterial
        fields = {
            'room_floor_material_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'floor_material': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class RoomImageFilter(filters.FilterSet):
    class Meta:
        model = models.RoomImage
        fields = {
            'room_image_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'image': NUMBER_FILTER_LIST,
            'description': CHAR_FILTER_LIST,
        }


class RoomSlotFilter(filters.FilterSet):
    class Meta:
        model = models.RoomSlot
        fields = {
            'room_slot_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'date': DATE_FILTER_LIST,
            'time_begin': TIME_FILTER_LIST,
            'time_end': TIME_FILTER_LIST,
            'workload': NUMBER_FILTER_LIST,
            'slot_price': NUMBER_FILTER_LIST,
            'remain_slot_count': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class RoomSlotDayTemplateFilter(filters.FilterSet):
    class Meta:
        model = models.RoomSlotDayTemplate
        fields = {
            'room_slot_day_template_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'day_template': NUMBER_FILTER_LIST,
            'time_begin': TIME_FILTER_LIST,
            'time_end': TIME_FILTER_LIST,
            'workload': NUMBER_FILTER_LIST,
            'slot_base_price': NUMBER_FILTER_LIST,
            'slot_count': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StationFilter(filters.FilterSet):
    class Meta:
        model = models.Station
        fields = {
            'station_id': NUMBER_FILTER_LIST,
            'station_name': CHAR_FILTER_LIST,
        }


class StationRailwayFilter(filters.FilterSet):
    class Meta:
        model = models.StationRailway
        fields = {
            'station_railway_id': NUMBER_FILTER_LIST,
            'station': NUMBER_FILTER_LIST,
            'railway': NUMBER_FILTER_LIST,
        }


class StationRailwayExitFilter(filters.FilterSet):
    class Meta:
        model = models.StationRailwayExit
        fields = {
            'station_railway_exit_id': NUMBER_FILTER_LIST,
            'station_railway': NUMBER_FILTER_LIST,
            'exit': NUMBER_FILTER_LIST,
        }


class StationRailwayLineFilter(filters.FilterSet):
    class Meta:
        model = models.StationRailwayLine
        fields = {
            'station_railway_line_id': NUMBER_FILTER_LIST,
            'station_railway': NUMBER_FILTER_LIST,
            'line': NUMBER_FILTER_LIST,
        }


class StudioFilter(filters.FilterSet):
    class Meta:
        model = models.Studio
        fields = {
            'studio_id': NUMBER_FILTER_LIST,
            'studio_name': CHAR_FILTER_LIST,
            'introduction': CHAR_FILTER_LIST,
            'precaution': CHAR_FILTER_LIST,
            'homepage_url': CHAR_FILTER_LIST,
            'contact': CHAR_FILTER_LIST,
            'address': NUMBER_FILTER_LIST,
            'rent_by_min_hours': NUMBER_FILTER_LIST,
            'can_free_cancel': BOOLEAN_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioAmenityFilter(filters.FilterSet):
    class Meta:
        model = models.StudioAmenity
        fields = {
            'studio_amenity_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'amenity': NUMBER_FILTER_LIST,
            'studio_amenity_serial_number': NUMBER_FILTER_LIST,
            'studio_amenity_description': CHAR_FILTER_LIST,
            'studio_amenity_count': NUMBER_FILTER_LIST,
            'studio_amenity_price': NUMBER_FILTER_LIST,
            'studio_amenity_unit_hour': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioFacilityFilter(filters.FilterSet):
    class Meta:
        model = models.StudioFacility
        fields = {
            'studio_facility_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'facility': NUMBER_FILTER_LIST,
            'studio_facility_serial_number': NUMBER_FILTER_LIST,
            'studio_facility_description': CHAR_FILTER_LIST,
            'studio_facility_count': NUMBER_FILTER_LIST,
            'studio_facility_price': NUMBER_FILTER_LIST,
            'studio_facility_unit_hour': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioImageFilter(filters.FilterSet):
    class Meta:
        model = models.StudioImage
        fields = {
            'studio_image_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'image': NUMBER_FILTER_LIST,
            'description': CHAR_FILTER_LIST,
        }


class StudioPaymentFilter(filters.FilterSet):
    class Meta:
        model = models.StudioPayment
        fields = {
            'studio_payment_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'payment': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioReservationFilter(filters.FilterSet):
    class Meta:
        model = models.StudioReservation
        fields = {
            'studio_reservation_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'reservation': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioStationRailwayExitFilter(filters.FilterSet):
    class Meta:
        model = models.StudioStationRailwayExit
        fields = {
            'studio_station_railway_exit_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'station_railway_exit': NUMBER_FILTER_LIST,
            'minutes_from_station': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }
