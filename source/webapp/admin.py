from django.contrib import admin

from accounts.models import Profile, Driver, Country, City
from webapp.models import Ad, Photo

admin.site.register(Profile)
admin.site.register(Driver)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Ad)
admin.site.register(Photo)

