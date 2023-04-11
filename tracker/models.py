from django.contrib.auth.models import User
from django.db import models
from django_admin_geomap import GeoItem
from geopy.geocoders import Nominatim

class Device(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.name}"


class Location(models.Model, GeoItem):
    address = models.CharField(max_length=100, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    lon = models.FloatField()  # долгота
    lat = models.FloatField()  # широта

    def __str__(self):
        return f"{self.device} - {self.address}"

    def get_address(self, lat, lan):
        geolocator = Nominatim(user_agent="myapp")
        location = geolocator.reverse(f"{lat}, {lan}")
        return location.address

    def save(self):

        lat = self.lat
        lng = self.lon
        address = self.get_address(lat, lng)
        self.address = address
        super().save()


    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)

    @property
    def geomap_icon(self):
        return self.default_icon

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view
