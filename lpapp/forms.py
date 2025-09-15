from django import forms
from .models import Appointment,Immigration
from .models import Webinar
from .models import Team
from .models import Review,Careers,AdmissionPartner

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class WebinarForm(forms.ModelForm):
    class Meta:
        model = Webinar
        fields = ['name','mail']     



class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'phone', 'img','bio','post'] 


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Immigration
        fields = '__all__'



class CareersForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = ['job_title', 'job_mode', 'job_salary', 'job_location', 'job_type', 'job_exp', 'job_details']  

class AdmissionPartnerForm(forms.ModelForm):
    class Meta:
        model = AdmissionPartner
        fields = '__all__'            