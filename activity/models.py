# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    number_of_college = models.IntegerField(blank=True, null=True)
    activity_plan = models.ForeignKey('ActivityPlan', models.DO_NOTHING, blank=True, null=True,
                                      related_name='activity_plan_name')
    content = models.TextField('活动内容', blank=True, null=True)
    car = models.ForeignKey('MallCar', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField('开始时间', blank=True, null=True)
    end_date = models.DateTimeField('结束时间', blank=True, null=True)
    add_money_for_benifit = models.FloatField(blank=True, null=True)
    activity_discount = models.FloatField(blank=True, null=True)
    market_discount = models.FloatField(blank=True, null=True)
    number_of_order = models.IntegerField(blank=True, null=True)
    front_image = models.CharField(max_length=50, blank=True, null=True)
    pay_money = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    watch_num = models.IntegerField('访问人数', blank=True, null=True)
    attent_num = models.IntegerField(blank=True, null=True)
    activity_price = models.FloatField('活动价格', blank=True, null=True)
    market_price = models.FloatField('市场价格', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'

    def __str__(self):
        return str(self.name)


class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    image_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_image'
        unique_together = (('activity', 'image'),)


class ActivityPlan(models.Model):
    dealer = models.ForeignKey('CarDealer', models.DO_NOTHING)
    create_plan_time = models.DateTimeField(blank=True, null=True)
    modify_plan_time = models.DateTimeField(blank=True, null=True)
    activity_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    city = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, blank=True, null=True)
    plan_status = models.IntegerField(blank=True, null=True)
    push_mode = models.IntegerField(blank=True, null=True)
    watch_start_time = models.DateField(blank=True, null=True)
    watch_end_time = models.DateField(blank=True, null=True)
    intention_attributes = models.CharField(max_length=50, blank=True, null=True)
    sexs = models.PositiveIntegerField(blank=True, null=True)
    ages = models.PositiveIntegerField(blank=True, null=True)
    cars = models.TextField(blank=True, null=True)
    push_freq = models.IntegerField(blank=True, null=True)
    time_interval = models.IntegerField(blank=True, null=True)
    start_push_with_workingday = models.TimeField(blank=True, null=True)
    end_push_with_workingday = models.TimeField(blank=True, null=True)
    start_push_with_holiday = models.TimeField(blank=True, null=True)
    end_push_with_holiday = models.TimeField(blank=True, null=True)
    push_cover_num = models.IntegerField(blank=True, null=True)
    push_cover_percent = models.IntegerField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_plan'

    def __str__(self):
        return str(self.activity_name)


class ActivitySummary(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING)
    date_time = models.DateField()
    number_of_order = models.IntegerField(blank=True, null=True)
    watch_num = models.IntegerField(blank=True, null=True)
    attent_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_summary'
        unique_together = (('activity', 'date_time'),)


class MallCar(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    oil_lost = models.CharField(max_length=50, blank=True, null=True)
    car_type = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    nums = models.CharField(max_length=50, blank=True, null=True)
    engine = models.CharField(max_length=50, blank=True, null=True)
    change_box = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_car'

    def __str__(self):
        return self.name


class CarDealer(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    province = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True, related_name='cardealer_province')
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


class District(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'

    def __str__(self):
        return self.name


class ManufacturerName(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer_name'

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return self.name
