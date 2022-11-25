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

    # Queries
    re_path(r'^query01$',views.query01Api),
    re_path(r'^query01/([0-9]+)$',views.query01Api),
    

    re_path(r'^query02$',views.query02Api),
    re_path(r'^query02/([0-9]+)$',views.query02Api),

    re_path(r'^query03$',views.query03Api),
    re_path(r'^query03/([0-9]+)$',views.query03Api),

    re_path(r'^query04$',views.query04Api),
    re_path(r'^query04/([0-9]+)$',views.query04Api),

    re_path(r'^query05$',views.query05Api),
    re_path(r'^query05/([0-9]+)$',views.query05Api),

    re_path(r'^query07$',views.query07Api),
    re_path(r'^query07/([0-9]+)$',views.query07Api),

]

