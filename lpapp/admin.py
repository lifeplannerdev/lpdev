from django.contrib import admin
from . models import Appointment
from . models import Webinar
from . models import Careers
from . models import Immigration
from . models import AdmissionPartner
from . models import FranchisePartner



# Register your models here.
admin.site.register(Appointment)
admin.site.register(Immigration)
admin.site.register(Webinar)
admin.site.register(Careers)
admin.site.register(AdmissionPartner)
admin.site.register(FranchisePartner)
