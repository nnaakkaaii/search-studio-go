from rest_framework import serializers

from search import models


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Slot
        fields = "__all__"


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Amenity
        fields = "__all__"


class RoomFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomFacility
        fields = "__all__"


class StudioFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudioFacility
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = "__all__"


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Station
        fields = "__all__"


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Line
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = "__all__"


class PrefectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prefecture
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = "__all__"


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Studio
        fields = "__all__"
