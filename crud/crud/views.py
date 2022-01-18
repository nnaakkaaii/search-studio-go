from rest_framework import viewsets

from crud import filters
from crud import models
from crud import serializers


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    filter_class = filters.AddressFilter


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = models.Amenity.objects.all()
    serializer_class = serializers.AmenitySerializer
    filter_class = filters.AmenityFilter


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    filter_class = filters.CityFilter


class DayTemplateViewSet(viewsets.ModelViewSet):
    queryset = models.DayTemplate.objects.all()
    serializer_class = serializers.DayTemplateSerializer
    filter_class = filters.DayTemplateFilter


class ExitViewSet(viewsets.ModelViewSet):
    queryset = models.Exit.objects.all()
    serializer_class = serializers.ExitSerializer
    filter_class = filters.ExitFilter


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = models.Facility.objects.all()
    serializer_class = serializers.FacilitySerializer
    filter_class = filters.FacilityFilter


class FloorMaterialViewSet(viewsets.ModelViewSet):
    queryset = models.FloorMaterial.objects.all()
    serializer_class = serializers.FloorMaterialSerializer
    filter_class = filters.FloorMaterialFilter


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    filter_class = filters.ImageFilter


class LineViewSet(viewsets.ModelViewSet):
    queryset = models.Line.objects.all()
    serializer_class = serializers.LineSerializer
    filter_class = filters.LineFilter


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    filter_class = filters.PaymentFilter


class PrefectureViewSet(viewsets.ModelViewSet):
    queryset = models.Prefecture.objects.all()
    serializer_class = serializers.PrefectureSerializer
    filter_class = filters.PrefectureFilter


class RailwayViewSet(viewsets.ModelViewSet):
    queryset = models.Railway.objects.all()
    serializer_class = serializers.RailwaySerializer
    filter_class = filters.RailwayFilter


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer
    filter_class = filters.ReservationFilter


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    filter_class = filters.RoomFilter


class RoomFacilityViewSet(viewsets.ModelViewSet):
    queryset = models.RoomFacility.objects.all()
    serializer_class = serializers.RoomFacilitySerializer
    filter_class = filters.RoomFacilityFilter


class RoomFloorMaterialViewSet(viewsets.ModelViewSet):
    queryset = models.RoomFloorMaterial.objects.all()
    serializer_class = serializers.RoomFloorMaterialSerializer
    filter_class = filters.RoomFloorMaterialFilter


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = models.RoomImage.objects.all()
    serializer_class = serializers.RoomImageSerializer
    filter_class = filters.RoomImageFilter


class RoomSlotViewSet(viewsets.ModelViewSet):
    queryset = models.RoomSlot.objects.all()
    serializer_class = serializers.RoomSlotSerializer
    filter_class = filters.RoomSlotFilter


class RoomSlotDayTemplateViewSet(viewsets.ModelViewSet):
    queryset = models.RoomSlotDayTemplate.objects.all()
    serializer_class = serializers.RoomSlotDayTemplateSerializer
    filter_class = filters.RoomSlotDayTemplateFilter


class StationViewSet(viewsets.ModelViewSet):
    queryset = models.Station.objects.all()
    serializer_class = serializers.StationSerializer
    filter_class = filters.StationFilter


class StationRailwayViewSet(viewsets.ModelViewSet):
    queryset = models.StationRailway.objects.all()
    serializer_class = serializers.StationRailwaySerializer
    filter_class = filters.StationRailwayFilter


class StationRailwayExitViewSet(viewsets.ModelViewSet):
    queryset = models.StationRailwayExit.objects.all()
    serializer_class = serializers.StationRailwayExitSerializer
    filter_class = filters.StationRailwayExitFilter


class StationRailwayLineViewSet(viewsets.ModelViewSet):
    queryset = models.StationRailwayLine.objects.all()
    serializer_class = serializers.StationRailwayLineSerializer
    filter_class = filters.StationRailwayLineFilter


class StudioViewSet(viewsets.ModelViewSet):
    queryset = models.Studio.objects.all()
    serializer_class = serializers.StudioSerializer
    filter_class = filters.StudioFilter


class StudioAmenityViewSet(viewsets.ModelViewSet):
    queryset = models.StudioAmenity.objects.all()
    serializer_class = serializers.StudioAmenitySerializer
    filter_class = filters.StudioAmenityFilter


class StudioFacilityViewSet(viewsets.ModelViewSet):
    queryset = models.StudioFacility.objects.all()
    serializer_class = serializers.StudioFacilitySerializer
    filter_class = filters.StudioFacilityFilter


class StudioImageViewSet(viewsets.ModelViewSet):
    queryset = models.StudioImage.objects.all()
    serializer_class = serializers.StudioImageSerializer
    filter_class = filters.StudioImageFilter


class StudioPaymentViewSet(viewsets.ModelViewSet):
    queryset = models.StudioPayment.objects.all()
    serializer_class = serializers.StudioPaymentSerializer
    filter_class = filters.StudioPaymentFilter


class StudioReservationViewSet(viewsets.ModelViewSet):
    queryset = models.StudioReservation.objects.all()
    serializer_class = serializers.StudioReservationSerializer
    filter_class = filters.StudioReservationFilter


class StudioStationRailwayExitViewSet(viewsets.ModelViewSet):
    queryset = models.StudioStationRailwayExit.objects.all()
    serializer_class = serializers.StudioStationRailwayExitSerializer
    filter_class = filters.StudioStationRailwayExitFilter
