from django.contrib import admin
from . models import Appointment
from . models import Webinar
from . models import Immigration

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Immigration)
admin.site.register(Webinar)
