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
    address_name = models.CharField(unique=True, max_length=1024)
    city = models.ForeignKey('City', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'address'


class Amenity(models.Model):
    amenity_id = models.AutoField(primary_key=True)
    amenity_name = models.CharField(unique=True, max_length=128)

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
        unique_together = (('city_name', 'prefecture'),)


class DayTemplate(models.Model):
    day_template_id = models.IntegerField(primary_key=True)
    day_template_name = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'day_template'


class Exit(models.Model):
    exit_id = models.AutoField(primary_key=True)
    exit_name = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'exit'


class Facility(models.Model):
    facility_id = models.AutoField(primary_key=True)
    facility_name = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'facility'


class FloorMaterial(models.Model):
    floor_material_id = models.AutoField(primary_key=True)
    floor_material_name = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'floor_material'


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=512)
    image_path = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'image'
        unique_together = (('image_name', 'image_path'),)


class Line(models.Model):
    line_id = models.AutoField(primary_key=True)
    line_name = models.CharField(unique=True, max_length=256)

    class Meta:
        managed = False
        db_table = 'line'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_name = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'payment'


class Prefecture(models.Model):
    prefecture_id = models.AutoField(primary_key=True)
    prefecture_name = models.CharField(unique=True, max_length=256)

    class Meta:
        managed = False
        db_table = 'prefecture'


class Railway(models.Model):
    railway_id = models.AutoField(primary_key=True)
    railway_name = models.CharField(unique=True, max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'railway'


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    reservation_name = models.CharField(unique=True, max_length=128)

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
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room'
        unique_together = (('studio', 'room_name'),)


class RoomFacility(models.Model):
    room_facility_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    room_facility_serial_number = models.IntegerField()
    room_facility_description = models.TextField(blank=True, null=True)
    room_facility_count = models.IntegerField(blank=True, null=True)
    room_facility_price = models.FloatField(blank=True, null=True)
    room_facility_unit_hour = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room_facility'
        unique_together = (('room', 'facility', 'room_facility_serial_number'),)


class RoomFloorMaterial(models.Model):
    room_floor_material_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    floor_material = models.ForeignKey(FloorMaterial, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room_floor_material'
        unique_together = (('room', 'floor_material'),)


class RoomImage(models.Model):
    room_image_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    image = models.ForeignKey(Image, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_image'
        unique_together = (('room', 'image'),)


class RoomSlot(models.Model):
    room_slot_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    date = models.DateField()
    time_begin = models.TimeField()
    time_end = models.TimeField()
    workload = models.FloatField()
    slot_price = models.FloatField()
    remain_slot_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room_slot'
        unique_together = (('room', 'date', 'time_begin'), ('room', 'date', 'time_end'),)


class RoomSlotDayTemplate(models.Model):
    room_slot_day_template_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    day_template = models.ForeignKey(DayTemplate, models.DO_NOTHING)
    time_begin = models.TimeField()
    time_end = models.TimeField()
    workload = models.FloatField()
    slot_base_price = models.FloatField()
    slot_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room_slot_day_template'
        unique_together = (('room', 'day_template', 'time_begin'), ('room', 'day_template', 'time_end'),)


class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(unique=True, max_length=256)

    class Meta:
        managed = False
        db_table = 'station'


class StationRailway(models.Model):
    station_railway_id = models.AutoField(primary_key=True)
    station = models.ForeignKey(Station, models.DO_NOTHING)
    railway = models.ForeignKey(Railway, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'station_railway'
        unique_together = (('station', 'railway'),)


class StationRailwayExit(models.Model):
    station_railway_exit_id = models.AutoField(primary_key=True)
    station_railway = models.ForeignKey(StationRailway, models.DO_NOTHING)
    exit = models.ForeignKey(Exit, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'station_railway_exit'
        unique_together = (('station_railway', 'exit'),)


class StationRailwayLine(models.Model):
    station_railway_line_id = models.AutoField(primary_key=True)
    station_railway = models.ForeignKey(StationRailway, models.DO_NOTHING)
    line = models.ForeignKey(Line, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'station_railway_line'
        unique_together = (('station_railway', 'line'),)


class Studio(models.Model):
    studio_id = models.AutoField(primary_key=True)
    studio_name = models.CharField(unique=True, max_length=1024)
    introduction = models.TextField(blank=True, null=True)
    precaution = models.TextField(blank=True, null=True)
    homepage_url = models.CharField(max_length=1024, blank=True, null=True)
    contact = models.CharField(max_length=11)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    rent_by_min_hours = models.FloatField()
    can_free_cancel = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio'


class StudioAmenity(models.Model):
    studio_amenity_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    amenity = models.ForeignKey(Amenity, models.DO_NOTHING)
    studio_amenity_serial_number = models.IntegerField()
    studio_amenity_description = models.TextField(blank=True, null=True)
    studio_amenity_count = models.IntegerField(blank=True, null=True)
    studio_amenity_price = models.FloatField(blank=True, null=True)
    studio_amenity_unit_hour = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_amenity'
        unique_together = (('studio', 'amenity', 'studio_amenity_serial_number'),)


class StudioFacility(models.Model):
    studio_facility_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    studio_facility_serial_number = models.IntegerField()
    studio_facility_description = models.TextField(blank=True, null=True)
    studio_facility_count = models.IntegerField(blank=True, null=True)
    studio_facility_price = models.FloatField(blank=True, null=True)
    studio_facility_unit_hour = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_facility'
        unique_together = (('studio', 'facility', 'studio_facility_serial_number'),)


class StudioImage(models.Model):
    studio_image_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    image = models.ForeignKey(Image, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studio_image'
        unique_together = (('studio', 'image'),)


class StudioPayment(models.Model):
    studio_payment_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    payment = models.ForeignKey(Payment, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_payment'
        unique_together = (('studio', 'payment'),)


class StudioReservation(models.Model):
    studio_reservation_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_reservation'
        unique_together = (('studio', 'reservation'),)


class StudioStationRailwayExit(models.Model):
    studio_station_railway_exit_id = models.AutoField(primary_key=True)
    studio = models.ForeignKey(Studio, models.DO_NOTHING)
    station_railway_exit = models.ForeignKey(StationRailwayExit, models.DO_NOTHING)
    minutes_from_station = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'studio_station_railway_exit'
        unique_together = (('studio', 'station_railway_exit'),)

