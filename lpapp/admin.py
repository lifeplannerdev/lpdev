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
# ADD THIS TO YOUR admin.py
# (paste alongside your existing admin registrations)

from django.contrib import admin
from .models import ConsultationRequest

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display   = ('name', 'phone', 'email', 'program', 'created_at', 'is_read')
    list_filter    = ('is_read', 'created_at')
    search_fields  = ('name', 'email', 'phone', 'program')
    readonly_fields = ('name', 'phone', 'email', 'program', 'message', 'created_at')
    ordering       = ('-created_at',)
    actions        = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = 'Mark selected as read'