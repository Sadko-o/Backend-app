# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from HospitalManagementApp.models import *
from HospitalManagementApp.serializers import *

# def diseaseTypeApi(request):
#     if request.method=='GET':
#         diseaseType = DiseaseType.objects.all()
#         diseaseType_serializer = DiseaseTypeSerializer(diseaseType,many=True)
#         res = JsonResponse(diseaseType_serializer.data,safe=False)
#         return res
#     elif request.method=='POST':
#         diseaseType_data=JSONParser().parse(request)
#         diseaseType_serializer=DiseaseTypeSerializer(data=diseaseType_data)
#         if diseaseType_serializer.is_valid():
#             diseaseType_serializer.save()
#             return JsonResponse("Added successfully",safe=False)
#         return JsonResponse("Failed to add", safe=False)
#     elif request.method=='PUT':
#         diseaseType_data=JSONParser().parse(request)
#         diseaseType=DiseaseType.objects.get(DiseaseTypeId=diseaseType_data['DiseaseTypeId'])
#         diseaseType_serializer=DiseaseTypeSerializer(diseaseType,data=diseaseType_data)
#         if diseaseType_serializer.is_valid():
#             diseaseType_serializer.save()
#             return JsonResponse("Updates successfully",safe=False)
#         return JsonResponse("Failed to update", safe=False)
#     elif request.method=='DELETE':
#         diseaseType_data=JSONParser().parse(request)
#         diseaseType=DiseaseType.objects.get(DiseaseTypeId=diseaseType_data['DiseaseTypeId'])
#         diseaseType.delete()
#         return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def diseaseTypeApi(request):


    if request.method=='GET':
        diseaseTypes = DiseaseType.objects.all()
        diseaseTypes_serializer=DiseaseTypeSerializer(diseaseTypes,many=True)
        return JsonResponse(diseaseTypes_serializer.data,safe=False)

    elif request.method=='POST':
        diseaseType_data=JSONParser().parse(request)
        diseaseTypes_serializer=DiseaseTypeSerializer(data=diseaseType_data)
        if diseaseTypes_serializer.is_valid():
            diseaseTypes_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        diseaseType_data=JSONParser().parse(request)
        diseaseTypes=DiseaseType.objects.get(diseaseTypeId=diseaseType_data['diseaseTypeId'])
        diseaseTypes_serializer=DiseaseTypeSerializer(diseaseTypes,data=diseaseType_data)
        if diseaseTypes_serializer.is_valid():
            diseaseTypes_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        diseaseType_data=JSONParser().parse(request)
        diseaseType=DiseaseType.objects.get(diseaseTypeId=diseaseType_data['diseaseTypeId'])
        diseaseType.delete()
        return JsonResponse("Deleted Successfully",safe=False)




@csrf_exempt
def countryApi(request):
    if request.method=='GET':
        countries = Country.objects.all()
        countries_serializer = CountrySerializer(countries,many=True)
        return JsonResponse(countries_serializer.data,safe=False)

    elif request.method=='POST':
        country_data=JSONParser().parse(request)
        country_serializer=CountrySerializer(data=country_data)
        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        country_data=JSONParser().parse(request)
        country=Country.objects.get(cname=country_data['cname'])
        countries_serializer=CountrySerializer(country,data=country_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update", safe=True)

    elif request.method=='DELETE':
        country_data=JSONParser().parse(request)
        country=Country.objects.get(cname=country_data['cname'])
        country.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def diseaseApi(request):
    if request.method=='GET':
        diseases = Disease.objects.all()
        diseases_serializer = DiseaseSerializer(diseases,many=True)
        return JsonResponse(diseases_serializer.data,safe=False)

    elif request.method=='POST':
        disease_data=JSONParser().parse(request)
        disease_serializer=DiseaseSerializer(data=disease_data)
        if disease_serializer.is_valid():
            disease_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        disease_data=JSONParser().parse(request)
        disease=Disease.objects.get(disease_code=disease_data['disease_code'])
        disease_serializer=DiseaseSerializer(disease,data=disease_data)
        if disease_serializer.is_valid():
            disease_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update", safe=True)

    elif request.method=='DELETE':
        disease_data=JSONParser().parse(request)
        disease=Disease.objects.get(disease_code=disease_data['disease_code'])
        disease.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def discoverApi(request):
    if request.method=='GET':
        discovers = Discover.objects.all()
        discovers_serializer = DiscoverSerializer(discovers,many=True)
        return JsonResponse(discovers_serializer.data,safe=False)

    elif request.method=='POST':
        discover_data=JSONParser().parse(request)
        discover_serializer=DiscoverSerializer(data=discover_data)
        if discover_serializer.is_valid():
            discover_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        discover_data=JSONParser().parse(request)
        discover=Discover.objects.get(cname=discover_data['cname'])
        discover_serializer=DiscoverSerializer(discover,data=discover_data)
        if discover_serializer.is_valid():
            discover_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update", safe=True)

    elif request.method=='DELETE':
        discover_data=JSONParser().parse(request)
        discover=Discover.objects.get(cname=discover_data['cname'])
        discover.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
@csrf_exempt
def usersApi(request):
    if request.method=='GET':
        users = Country.objects.all()
        users_serializer = CountrySerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)

    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer=CountrySerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        user_data=JSONParser().parse(request)
        user=Country.objects.get(email=user_data['email'])
        user_serializer=CountrySerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update", safe=True)

    elif request.method=='DELETE':
        user_data=JSONParser().parse(request)
        user=Country.objects.get(email=user_data['email'])
        user.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def publicServantApi(request):
    if request.method=='GET':
        publicServants = PublicServant.objects.all()
        publicServants_serializer = PublicServantSerializer(publicServants,many=True)
        return JsonResponse(publicServants_serializer.data,safe=False)

    elif request.method=='POST':
        publicServant_data=JSONParser().parse(request)
        publicServant_serializer=PublicServantSerializer(data=publicServant_data)
        if publicServant_serializer.is_valid():
            publicServant_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        publicServant_data=JSONParser().parse(request)
        publicServant=PublicServant.objects.get(email=publicServant_data['email'])
        publicServants_serializer=PublicServantSerializer(publicServant,data=publicServant_data)
        if publicServants_serializer.is_valid():
            publicServants_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update", safe=True)

    elif request.method=='DELETE':
        publicServant_data=JSONParser().parse(request)
        publicServant=PublicServant.objects.get(email=publicServant_data['email'])
        publicServant.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def doctorApi(request):
    if request.method=='GET':
        doctors = Doctor.objects.all()
        doctors_serializer = DoctorSerializer(doctors,many=True)
        return JsonResponse(doctors_serializer.data,safe=False)

    elif request.method=='POST':
        doctor_data=JSONParser().parse(request)
        doctor_serializer=DoctorSerializer(data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        doctor_data=JSONParser().parse(request)
        doctor=Doctor.objects.get(email=doctor_data['email'])
        doctors_serializer=DoctorSerializer(doctor,data=doctor_data)
        if doctors_serializer.is_valid():
            doctors_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update", safe=True)

    elif request.method=='DELETE':
        doctor_data=JSONParser().parse(request)
        doctor=Doctor.objects.get(email=doctor_data['email'])
        doctor.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def specializeApi(request):
    if request.method=='GET':
        specializes = Specialize.objects.all()
        specializes_serializer = SpecializeSerializer(specializes,many=True)
        return JsonResponse(specializes_serializer.data,safe=False)

    elif request.method=='POST':
        specialize_data=JSONParser().parse(request)
        specialize_serializer=SpecializeSerializer(data=specialize_data)
        if specialize_serializer.is_valid():
            specialize_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        specialize_data=JSONParser().parse(request)
        specialize=Specialize.objects.get(diseaseTypeId=specialize_data['diseaseTypeId'])
        specializes_serializer=SpecializeSerializer(specialize,data=specialize_data)
        if specializes_serializer.is_valid():
            specializes_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update", safe=True)

    elif request.method=='DELETE':
        specialize_data=JSONParser().parse(request)
        specialize=Specialize.objects.get(diseaseTypeId=specialize_data['diseaseTypeId'])
        specialize.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def recordApi(request):
    if request.method=='GET':
        records = Record.objects.all()
        records_serializer = RecordSerializer(records,many=True)
        return JsonResponse(records_serializer.data,safe=False)

    elif request.method=='POST':
        record_data=JSONParser().parse(request)
        record_serializer=RecordSerializer(data=record_data)
        if record_serializer.is_valid():
            record_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        record_data=JSONParser().parse(request)
        record=Record.objects.get(email=record_data['email'])
        records_serializer=RecordSerializer(record,data=record_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update", safe=True)

    elif request.method=='DELETE':
        record_data=JSONParser().parse(request)
        record=Record.objects.get(email=record_data['email'])
        record.delete()
        return JsonResponse("Deleted Successfully",safe=False)

