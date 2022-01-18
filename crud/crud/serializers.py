from rest_framework import serializers

from crud import models


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Amenity
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = '__all__'


class DayTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DayTemplate
        fields = '__all__'


class ExitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Exit
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Facility
        fields = '__all__'


class FloorMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FloorMaterial
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


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Payment
        fields = '__all__'


class PrefectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Prefecture
        fields = '__all__'


class RailwaySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Railway
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reservation
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class RoomFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomFacility
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class RoomFloorMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomFloorMaterial
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class RoomImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomImage
        fields = '__all__'


class RoomSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomSlot
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class RoomSlotDayTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomSlotDayTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Station
        fields = '__all__'


class StationRailwaySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailway
        fields = '__all__'


class StationRailwayExitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailwayExit
        fields = '__all__'


class StationRailwayLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StationRailwayLine
        fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Studio
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioAmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioAmenity
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioFacility
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioImage
        fields = '__all__'


class StudioPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioPayment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioReservation
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class StudioStationRailwayExitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudioStationRailwayExit
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
