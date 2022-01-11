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


class DateSlotLinkViewSet(viewsets.ModelViewSet):
    queryset = models.DateSlotLink.objects.all()
    serializer_class = serializers.DateSlotLinkSerializer
    filter_class = filters.DateSlotLinkFilter


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


class RoomFacilityLinkViewSet(viewsets.ModelViewSet):
    queryset = models.RoomFacilityLink.objects.all()
    serializer_class = serializers.RoomFacilityLinkSerializer
    filter_class = filters.RoomFacilityLinkFilter


class RoomFloorMaterialLinkViewSet(viewsets.ModelViewSet):
    queryset = models.RoomFloorMaterialLink.objects.all()
    serializer_class = serializers.RoomFloorMaterialLinkSerializer
    filter_class = filters.RoomFloorMaterialLinkFilter


class RoomImageLinkViewSet(viewsets.ModelViewSet):
    queryset = models.RoomImageLink.objects.all()
    serializer_class = serializers.RoomImageLinkSerializer
    filter_class = filters.RoomImageLinkFilter


class RoomSlotLinkViewSet(viewsets.ModelViewSet):
    queryset = models.RoomSlotLink.objects.all()
    serializer_class = serializers.RoomSlotLinkSerializer
    filter_class = filters.RoomSlotLinkFilter


class SlotViewSet(viewsets.ModelViewSet):
    queryset = models.Slot.objects.all()
    serializer_class = serializers.SlotSerializer
    filter_class = filters.SlotFilter


class SlotDayTemplateLinkViewSet(viewsets.ModelViewSet):
    queryset = models.SlotDayTemplateLink.objects.all()
    serializer_class = serializers.SlotDayTemplateLinkSerializer
    filter_class = filters.SlotDayTemplateLinkFilter


class StationViewSet(viewsets.ModelViewSet):
    queryset = models.Station.objects.all()
    serializer_class = serializers.StationSerializer
    filter_class = filters.StationFilter


class StationRailwayExitLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StationRailwayExitLink.objects.all()
    serializer_class = serializers.StationRailwayExitLinkSerializer
    filter_class = filters.StationRailwayExitLinkFilter


class StationRailwayLineLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StationRailwayLineLink.objects.all()
    serializer_class = serializers.StationRailwayLineLinkSerializer
    filter_class = filters.StationRailwayLineLinkFilter


class StationRailwayLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StationRailwayLink.objects.all()
    serializer_class = serializers.StationRailwayLinkSerializer
    filter_class = filters.StationRailwayLinkFilter


class StudioViewSet(viewsets.ModelViewSet):
    queryset = models.Studio.objects.all()
    serializer_class = serializers.StudioSerializer
    filter_class = filters.StudioFilter


class StudioAccessByStationLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StudioAccessByStationLink.objects.all()
    serializer_class = serializers.StudioAccessByStationLinkSerializer
    filter_class = filters.StudioAccessByStationLinkFilter


class StudioAmenityLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StudioAmenityLink.objects.all()
    serializer_class = serializers.StudioAmenityLinkSerializer
    filter_class = filters.StudioAmenityLinkFilter


class StudioFacilityLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StudioFacilityLink.objects.all()
    serializer_class = serializers.StudioFacilityLinkSerializer
    filter_class = filters.StudioFacilityLinkFilter


class StudioImageLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StudioImageLink.objects.all()
    serializer_class = serializers.StudioImageLinkSerializer
    filter_class = filters.StudioImageLinkFilter


class StudioPaymentLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StudioPaymentLink.objects.all()
    serializer_class = serializers.StudioPaymentLinkSerializer
    filter_class = filters.StudioPaymentLinkFilter


class StudioReservationLinkViewSet(viewsets.ModelViewSet):
    queryset = models.StudioReservationLink.objects.all()
    serializer_class = serializers.StudioReservationLinkSerializer
    filter_class = filters.StudioReservationLinkFilter
