from django.urls import re_path
from HospitalManagementApp import views


urlpatterns=[
    # DiseaseType
    re_path(r'^diseasetype$',views.diseaseTypeApi),
    re_path(r'^diseasetype/([0-9]+)$',views.diseaseTypeApi),

    # Country
    re_path(r'^country$',views.countryApi),
    re_path(r'^country/([0-9]+)$',views.countryApi),

    # Disease
    re_path(r'^disease$',views.diseaseApi),
    re_path(r'^disease/([0-9]+)$',views.diseaseApi),

    # Discover
    re_path(r'^discover$',views.discoverApi),
    re_path(r'^discover/([0-9]+)$',views.discoverApi),

    # Users
    re_path(r'^users$',views.usersApi),
    re_path(r'^users/([0-9]+)$',views.usersApi),

    # PublicServant
    re_path(r'^publicServant$',views.publicServantApi),
    re_path(r'^publicServant/([0-9]+)$',views.publicServantApi),

    # Doctor
    re_path(r'^doctor$',views.doctorApi),
    re_path(r'^doctor/([0-9]+)$',views.doctorApi),

    # Specialize
    re_path(r'^specialize$',views.specializeApi),
    re_path(r'^specialize/([0-9]+)$',views.specializeApi),

    # Record
    re_path(r'^record$',views.recordApi),
    re_path(r'^record/([0-9]+)$',views.recordApi),
]

