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


class DateSlotLinkFilter(filters.FilterSet):
    class Meta:
        model = models.DateSlotLink
        fields = {
            'date_slot_link_id': NUMBER_FILTER_LIST,
            'date': DATE_FILTER_LIST,
            'slot': NUMBER_FILTER_LIST,
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


class RoomFacilityLinkFilter(filters.FilterSet):
    class Meta:
        model = models.RoomFacilityLink
        fields = {
            'room_facility_link_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'facility': NUMBER_FILTER_LIST,
            'room_facility_count': NUMBER_FILTER_LIST,
            'room_facility_price': NUMBER_FILTER_LIST,
            'room_facility_unit_hour': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class RoomFloorMaterialLinkFilter(filters.FilterSet):
    class Meta:
        model = models.RoomFloorMaterialLink
        fields = {
            'room_floor_material_link_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'floor_material': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class RoomImageLinkFilter(filters.FilterSet):
    class Meta:
        model = models.RoomImageLink
        fields = {
            'room_image_link_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'image': NUMBER_FILTER_LIST,
            'description': CHAR_FILTER_LIST,
        }


class RoomSlotLinkFilter(filters.FilterSet):
    class Meta:
        model = models.RoomSlotLink
        fields = {
            'room_slot_link_id': NUMBER_FILTER_LIST,
            'room': NUMBER_FILTER_LIST,
            'date_slot_link': NUMBER_FILTER_LIST,
            'remain_slot_count': NUMBER_FILTER_LIST,
            'slot_price': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class SlotFilter(filters.FilterSet):
    class Meta:
        model = models.Slot
        fields = {
            'slot_id': NUMBER_FILTER_LIST,
            'workload': NUMBER_FILTER_LIST,
            'time_begin': TIME_FILTER_LIST,
            'time_end': TIME_FILTER_LIST,
            'slot_base_price': NUMBER_FILTER_LIST,
            'slot_count': NUMBER_FILTER_LIST,
        }


class SlotDayTemplateLinkFilter(filters.FilterSet):
    class Meta:
        model = models.SlotDayTemplateLink
        fields = {
            'slot_day_template_link_id': NUMBER_FILTER_LIST,
            'slot': NUMBER_FILTER_LIST,
            'day_template': NUMBER_FILTER_LIST,
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


class StationRailwayExitLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StationRailwayExitLink
        fields = {
            'station_railway_exit_link_id': NUMBER_FILTER_LIST,
            'station_railway_link': NUMBER_FILTER_LIST,
            'exit': NUMBER_FILTER_LIST,
        }


class StationRailwayLineLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StationRailwayLineLink
        fields = {
            'station_railway_line_link_id': NUMBER_FILTER_LIST,
            'station_railway_link': NUMBER_FILTER_LIST,
            'line': NUMBER_FILTER_LIST,
        }


class StationRailwayLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StationRailwayLink
        fields = {
            'station_railway_link_id': NUMBER_FILTER_LIST,
            'station': NUMBER_FILTER_LIST,
            'railway': NUMBER_FILTER_LIST,
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


class StudioAccessByStationLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StudioAccessByStationLink
        fields = {
            'studio_access_by_station_link_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'station_railway_exit_link': NUMBER_FILTER_LIST,
            'minutes_from_station': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioAmenityLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StudioAmenityLink
        fields = {
            'studio_amenity_link_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'amenity': NUMBER_FILTER_LIST,
            'studio_amenity_count': NUMBER_FILTER_LIST,
            'studio_amenity_price': NUMBER_FILTER_LIST,
            'studio_amenity_unit_hour': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioFacilityLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StudioFacilityLink
        fields = {
            'studio_facility_link_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'facility': NUMBER_FILTER_LIST,
            'studio_facility_count': NUMBER_FILTER_LIST,
            'studio_facility_price': NUMBER_FILTER_LIST,
            'studio_facility_unit_hour': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioImageLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StudioImageLink
        fields = {
            'studio_image_link_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'image': NUMBER_FILTER_LIST,
            'description': CHAR_FILTER_LIST,
        }


class StudioPaymentLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StudioPaymentLink
        fields = {
            'studio_payment_link_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'payment': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }


class StudioReservationLinkFilter(filters.FilterSet):
    class Meta:
        model = models.StudioReservationLink
        fields = {
            'studio_reservation_link_id': NUMBER_FILTER_LIST,
            'studio': NUMBER_FILTER_LIST,
            'reservation': NUMBER_FILTER_LIST,
            'created_at': DATETIME_FILTER_LIST,
            'updated_at': DATETIME_FILTER_LIST,
            'deleted_at': DATETIME_FILTER_LIST,
            'is_deleted': BOOLEAN_FILTER_LIST,
        }