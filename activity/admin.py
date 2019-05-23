from django.contrib import admin

# Register your models here.
from . import models


# class CarInline(admin.StackedInline):
#     model = models.MallCar


# admin.site.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('content', 'start_date')
    # ordering = ('-start_date')
    list_per_page = 10
    # prepopulated_fields = {}
    # inlines = [CarInline,]


# list_select_related = ['activity_plan']
admin.site.register(models.Activity, ActivityAdmin)
