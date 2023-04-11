from django.contrib import admin
from django_admin_geomap import ModelAdmin
from djangoql.admin import DjangoQLSearchMixin

from tracker.models import Location, Device


@admin.register(Device)
class DeviceAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('user',)
    preserve_filters = ('user',)


class Admin(DjangoQLSearchMixin, ModelAdmin):
    search_fields = ('id', 'device__name', 'device__user__username', 'address')
    readonly_fields = ('address',)
    list_display = ('id', 'address', 'device', 'timestamp',)
    list_filter = ('device',)
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_longitude = "69.58613644218235"
    geomap_default_latitude = "42.325406525793625"
    geomap_default_zoom = "13"
    geomap_item_zoom = "13"
    geomap_height = "500px"


admin.site.register(Location, Admin)
