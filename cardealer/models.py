from django.db import models


# Create your models here.
class CarDealer(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    province = models.ForeignKey('Province', models.DO_NOTHING, blank=True, null=True, related_name='cardealer_province')
    city = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True, related_name='cardealer_city')
    phone_num = models.CharField(max_length=100, blank=True, null=True)
    visitor_num = models.IntegerField(blank=True, null=True)
    call_phone_num = models.IntegerField(blank=True, null=True)
    buy_num = models.IntegerField(blank=True, null=True)
    manufacturer_name = models.ForeignKey('ManufacturerName', models.DO_NOTHING, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    dealer_image = models.CharField(max_length=255, blank=True, null=True)
    logo_image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_dealer'
    #返回值，使其不是object
    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey('Province', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'
    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True, related_name='province_region')

    class Meta:
        managed = False
        db_table = 'province'
    def __str__(self):
        return self.name


class ManufacturerName(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer_name'
    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'
    def __str__(self):
        return self.name
