from django.contrib import admin
from .models import *

# Register your models here.

class FlatAdmin(admin.ModelAdmin):
    list_display = ('roomtype', 'city')
    list_display_links = ('roomtype', 'city')
    search_fields = ('roomtype', 'city')


admin.site.register(Flat, FlatAdmin,)


class RoomtypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Roomtypes, RoomtypesAdmin)


class FreeplanAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Freeplan, FreeplanAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Country, CountryAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'pid')
    list_display_links = ('name', 'pid')


admin.site.register(Region, RegionAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'pid')
    list_display_links = ('name', 'pid')


admin.site.register(City, CityAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(District, DistrictAdmin)


class RepairtypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Repairtype, RepairtypeAdmin)


class WindowsviewAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Windowsview, WindowsviewAdmin)


class HousetypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Housetype, HousetypeAdmin)


class LifttypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Lifttype, LifttypeAdmin)


class ParkingtypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Parkingtype, ParkingtypeAdmin)


class SaletypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Saletype, SaletypeAdmin)


class SallertypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Sallertype, SallertypeAdmin)


class MertolineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Mertoline, MertolineAdmin)


class MetroAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Metro, MetroAdmin)


class FlatmetroAdmin(admin.ModelAdmin):
    list_display = ('flat', 'metro')
    list_display_links = ('flat', 'metro')


admin.site.register(Flatmetro, FlatmetroAdmin)