from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^doctorDashboard/', views.doctorDashboard, name='doctorDashboard'),
    url(r'^patientProfile/', views.patientProfile, name='patientProfile'),
    url(r'^doctorProfile/', views.doctorProfile, name='doctorProfile'),
    url(r'^patientDashboard/', views.patientDashboard, name='patientDashboard'),
    url(r'^patientDiagnosis/', views.patientDiagnosis, name='patientDiagnosis'),
    url(r'^doctorDiagnosis/', views.doctorDiagnosis, name='doctorDiagnosis'),
    url(r'^doctorAppointments/', views.doctorAppointments, name='doctorAppointments'),
    url(r'^patientAppointments/', views.patientAppointments, name='patientAppointments'),
    url(r'^addAppointment/', views.addAppointment, name='addAppointment'),
    url(r'^register/', views.register, name='register'),
    url(r'^updateProfile/', views.updateProfile, name='updateProfile'),
    url(r'^showDoctor/(?P<doctorId>[0-9]+)/$', views.showDoctor, name='showDoctor'),
]