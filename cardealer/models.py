from django.db import models

# Create your models here.
class CarDealer(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    province = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True)
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