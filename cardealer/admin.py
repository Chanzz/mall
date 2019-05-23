from django.contrib import admin

# Register your models here.
from . import models


class CarDealerAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(models.CarDealer, CarDealerAdmin)
