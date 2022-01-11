# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_name = models.CharField(max_length=1024)
    city = models.ForeignKey('City', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'address'


class Amenity(models.Model):
    amenity_id = models.AutoField(primary_key=True)
    amenity_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'amenity'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=256)
    prefecture = models.ForeignKey('Prefecture', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'city'


class DateSlotLink(models.Model):
    date_slot_link_id = models.AutoField(primary_key=True)
    date = models.DateField()
    slot = models.ForeignKey('Slot', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'date_slot_link'
        unique_together = (('date', 'slot'),)


class DayTemplate(models.Model):
    day_template_id = models.AutoField(primary_key=True)
    day_template_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'day_template'


class Exit(models.Model):
    exit_id = models.AutoField(primary_key=True)
    exit_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'exit'


class Facility(models.Model):
    facility_id = models.AutoField(primary_key=True)
    facility_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'facility'


class FloorMaterial(models.Model):
    floor_material_id = models.AutoField(primary_key=True)
    floor_material_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'floor_material'


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=512)
    image_path = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'image'


class Line(models.Model):
    line_id = models.AutoField(primary_key=True)
    line_name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'line'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'payment'


class Prefecture(models.Model):
    prefecture_id = models.AutoField(primary_key=True)
    prefecture_name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'prefecture'


class Railway(models.Model):
    railway_id = models.AutoField(primary_key=True)
    railway_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'railway'


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    reservation_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'reservation'


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey('Studio', models.DO_NOTHING)
    room_name = models.CharField(max_length=512)
    reservation_url = models.CharField(max_length=1024, blank=True, null=True)
    min_reservable_people = models.IntegerField(blank=True, null=True)
    max_reservable_people = models.IntegerField(blank=True, null=True)
    floor_area = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room'


class RoomFacilityLink(models.Model):
    room_facility_link_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    room_facility_count = models.IntegerField(blank=True, null=True)
    room_facility_price = models.FloatField(blank=True, null=True)
    room_facility_unit_hour = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room_facility_link'
        unique_together = (('room', 'facility'),)


class RoomFloorMaterialLink(models.Model):
    room_floor_material_link_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    floor_material = models.ForeignKey(FloorMaterial, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room_floor_material_link'
        unique_together = (('room', 'floor_material'),)


class RoomImageLink(models.Model):
    room_image_link_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    image = models.ForeignKey(Image, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_image_link'
        unique_together = (('room', 'image'),)


class RoomSlotLink(models.Model):
    room_slot_link_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    date_slot_link = models.ForeignKey(DateSlotLink, models.DO_NOTHING)
    remain_slot_count = models.IntegerField()
    slot_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room_slot_link'
        unique_together = (('room', 'date_slot_link'),)


class Slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    workload = models.FloatField()
    time_begin = models.TimeField()
    time_end = models.TimeField()
    slot_base_price = models.FloatField()
    slot_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slot'


class SlotDayTemplateLink(models.Model):
    slot_day_template_link_id = models.AutoField(primary_key=True)
    slot = models.ForeignKey(Slot, models.DO_NOTHING)
    day_template = models.ForeignKey(DayTemplate, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'slot_day_template_link'
        unique_together = (('slot', 'day_template'),)


class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'station'


class StationRailwayExitLink(models.Model):
    station_railway_exit_link_id = models.AutoField(primary_key=True)
    station_railway_link = models.ForeignKey('StationRailwayLink', models.DO_NOTHING)
    exit = models.ForeignKey(Exit, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'station_railway_exit_link'
        unique_together = (('station_railway_link', 'exit'),)


class StationRailwayLineLink(models.Model):
    station_railway_line_link_id = models.AutoField(primary_key=True)
    station_railway_link = models.ForeignKey('StationRailwayLink', models.DO_NOTHING)
    line = models.ForeignKey(Line, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'station_railway_line_link'
        unique_together = (('station_railway_link', 'line'),)


class StationRailwayLink(models.Model):
    station_railway_link_id = models.AutoField(primary_key=True)
    station = models.ForeignKey(Station, models.DO_NOTHING)
    railway = models.ForeignKey(Railway, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'station_railway_link'
        unique_together = (('station', 'railway'),)


class Studio(models.Model):
    studio_id = models.AutoField(primary_key=True)
    studio_name = models.CharField(max_length=1024)
    introduction = models.TextField(blank=True, null=True)
    precaution = models.TextField(blank=True, null=True)
    homepage_url = models.CharField(max_length=1024, blank=True, null=True)
    contact = models.CharField(max_length=11)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    rent_by_min_hours = models.FloatField()
    can_free_cancel = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio'


class StudioAccessByStationLink(models.Model):
    studio_access_by_station_link_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    station_railway_exit_link = models.ForeignKey(StationRailwayExitLink, models.DO_NOTHING)
    minutes_from_station = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_access_by_station_link'
        unique_together = (('studio', 'station_railway_exit_link'),)


class StudioAmenityLink(models.Model):
    studio_amenity_link_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    amenity = models.ForeignKey(Amenity, models.DO_NOTHING)
    studio_amenity_count = models.IntegerField(blank=True, null=True)
    studio_amenity_price = models.FloatField(blank=True, null=True)
    studio_amenity_unit_hour = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_amenity_link'
        unique_together = (('studio', 'amenity'),)


class StudioFacilityLink(models.Model):
    studio_facility_link_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    studio_facility_count = models.IntegerField(blank=True, null=True)
    studio_facility_price = models.FloatField(blank=True, null=True)
    studio_facility_unit_hour = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_facility_link'
        unique_together = (('studio', 'facility'),)


class StudioImageLink(models.Model):
    studio_image_link_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    image = models.ForeignKey(Image, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studio_image_link'
        unique_together = (('studio', 'image'),)


class StudioPaymentLink(models.Model):
    studio_payment_link_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    payment = models.ForeignKey(Payment, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_payment_link'
        unique_together = (('studio', 'payment'),)


class StudioReservationLink(models.Model):
    studio_reservation_link_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_reservation_link'
        unique_together = (('studio', 'reservation'),)

