from django.urls import path
from . import views
app_name='lpapp'

urlpatterns = [
   path('',views.home,name='home'),
   path('kochi/',views.kochi,name='kochi'),
   path('service/',views.service,name='service'),
   path('blog/',views.blog,name='blog'),
   path('teamupdate/', views.teamupdate, name='teamupdate'),
   path('partnering/', views.partnering, name='partnering'),
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
   path('blog4/',views.blog4,name='blog4'),
   path('blog5/',views.blog5,name='blog5'),
   path('blog6/',views.blog6,name='blog6'),
   path('blog7/',views.blog7,name='blog7'),
   path('blog8/',views.blog8,name='blog8'),
   path('blog9/',views.blog9,name='blog9'),
   path('demo/',views.demo,name='demo'),
   path('hrlp/',views.hrlp,name='hrlp'),
   path('careers/',views.careers,name='careers'),
   path('careers/<slug:slug>/',views.jobdetails, name='jobdetails'),
   path('uploadjob/',views.uploadjob,name='uploadjob'),
   path('applications/',views.job_applications,name='applications'),
   path("delete-application/<int:app_id>/",views.delete_application, name="delete_application"),

 
]