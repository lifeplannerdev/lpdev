from django.urls import path
from . import views
app_name='lpapp'

urlpatterns = [
   path('',views.home,name='home'),
   path('service/',views.service,name='service'),
   path('blog/',views.blog,name='blog'),
   path('teamupdate/', views.teamupdate, name='teamupdate'),
   path('profile/<int:pk>/', views.profile, name='profile'),
   path('albums/',views.albums,name='albums'),
   path('contact/',views.contact,name='contact'),
   path('canada/',views.canada,name='canada'),
   path('germany/',views.germany,name='germany'),
   path('studycanada/',views.studycanada,name='studycanada'),
   path('studyeurope/',views.studyeurope,name='studyeurope'),
   path('about/',views.about,name='about'),
   path('blog1/',views.blog1,name='blog1'),
   path('blog2/',views.blog2,name='blog2'),
   path('blog3/',views.blog3,name='blog3'),
   path('demo/',views.demo,name='demo'),
   path('careers/',views.careers,name='careers'),
   path('careers/<slug:slug>/',views.jobdetails, name='jobdetails'),
   path('uploadjob/',views.uploadjob,name='uploadjob'),

 
]