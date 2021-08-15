from django.contrib import admin

from search import models

# Register your models here.
@admin.register(models.Slot)
class SlotAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RoomFacility)
class RoomFacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StudioFacility)
class StudioFacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Station)
class StationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Line)
class LineAdmin(admin.ModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Prefecture)
class PrefectureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):
    pass
