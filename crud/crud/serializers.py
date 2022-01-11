from rest_framework import serializers

from crud import models


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Amenity
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Amenity
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = '__all__'


class DateSlotLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DateSlotLink
        fields = '__all__'


class DateSlotLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DateSlotLink
        fields = '__all__'


class DayTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DayTemplate
        fields = '__all__'


class DayTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DayTemplate
        fields = '__all__'


class ExitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Exit
        fields = '__all__'


class ExitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Exit
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Facility
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Facility
        fields = '__all__'


class FloorMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FloorMaterial
        fields = '__all__'


class FloorMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FloorMaterial
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Line
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Line
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Payment
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Payment
        fields = '__all__'


class PrefectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Prefecture
        fields = '__all__'


class PrefectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Prefecture
        fields = '__all__'


class RailwaySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Railway
        fields = '__all__'


class RailwaySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Railway
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reservation
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reservation
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class RoomFacilityLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomFacilityLink
        fields = '__all__'


class RoomFacilityLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomFacilityLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class RoomFloorMaterialLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomFloorMaterialLink
        fields = '__all__'


class RoomFloorMaterialLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomFloorMaterialLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class RoomImageLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomImageLink
        fields = '__all__'


class RoomImageLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomImageLink
        fields = '__all__'


class RoomSlotLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomSlotLink
        fields = '__all__'


class RoomSlotLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomSlotLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Slot
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Slot
        fields = '__all__'


class SlotDayTemplateLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlotDayTemplateLink
        fields = '__all__'


class SlotDayTemplateLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlotDayTemplateLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Station
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Station
        fields = '__all__'


class StationRailwayExitLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailwayExitLink
        fields = '__all__'


class StationRailwayExitLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailwayExitLink
        fields = '__all__'


class StationRailwayLineLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailwayLineLink
        fields = '__all__'


class StationRailwayLineLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailwayLineLink
        fields = '__all__'


class StationRailwayLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailwayLink
        fields = '__all__'


class StationRailwayLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailwayLink
        fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Studio
        fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Studio
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioAccessByStationLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioAccessByStationLink
        fields = '__all__'


class StudioAccessByStationLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioAccessByStationLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioAmenityLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioAmenityLink
        fields = '__all__'


class StudioAmenityLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioAmenityLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioFacilityLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioFacilityLink
        fields = '__all__'


class StudioFacilityLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioFacilityLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioImageLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioImageLink
        fields = '__all__'


class StudioImageLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioImageLink
        fields = '__all__'


class StudioPaymentLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioPaymentLink
        fields = '__all__'


class StudioPaymentLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioPaymentLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioReservationLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioReservationLink
        fields = '__all__'


class StudioReservationLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioReservationLink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
