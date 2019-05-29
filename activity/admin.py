from django.contrib import admin

# Register your models here.
from . import models


# class CarInline(admin.StackedInline):
#     model = models.MallCar


# admin.site.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    # 主页显示字段
    list_display = ('content', 'start_date')
    # 排序
    # ordering = ('-start_date')
    # 主页每页显示条数
    list_per_page = 10
    # prepopulated_fields = {}
    # inlines = [CarInline,]
    # fieldsets = ()


# list_select_related = ['activity_plan']
admin.site.register(models.Activity, ActivityAdmin)
