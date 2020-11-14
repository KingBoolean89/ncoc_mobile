from django.contrib import admin
from .models import *
# Register your models here.


class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'portion',)


class CenterAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DailyReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'large_group', 'small_group',
                    'story', 'art', 'music', 'needed_items', )


admin.site.register(Meal, MealAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(DailyReport, DailyReportAdmin)
