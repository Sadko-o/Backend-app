from django.core.files.storage import default_storage
from sqlalchemy import create_engine
from sqlalchemy import text
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from HospitalManagementApp.models import *
from HospitalManagementApp.serializers import *

# # def diseaseTypeApi(request):
# #     if request.method=='GET':
# #         diseaseType = DiseaseType.objects.all()
# #         diseaseType_serializer = DiseaseTypeSerializer(diseaseType,many=True)
# #         res = JsonResponse(diseaseType_serializer.data,safe=False)
# #         return res
# #     elif request.method=='POST':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseType_serializer=DiseaseTypeSerializer(data=diseaseType_data)
# #         if diseaseType_serializer.is_valid():
# #             diseaseType_serializer.save()
# #             return JsonResponse("Added successfully",safe=False)
# #         return JsonResponse("Failed to add", safe=False)
# #     elif request.method=='PUT':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseType=DiseaseType.objects.get(DiseaseTypeId=diseaseType_data['DiseaseTypeId'])
# #         diseaseType_serializer=DiseaseTypeSerializer(diseaseType,data=diseaseType_data)
# #         if diseaseType_serializer.is_valid():
# #             diseaseType_serializer.save()
# #             return JsonResponse("Updates successfully",safe=False)
# #         return JsonResponse("Failed to update", safe=False)
# #     elif request.method=='DELETE':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseType=DiseaseType.objects.get(DiseaseTypeId=diseaseType_data['DiseaseTypeId'])
# #         diseaseType.delete()
# #         return JsonResponse("Deleted successfully",safe=False)

# # @csrf_exempt
# # def diseaseTypeApi(request):
# #     if request.method=='GET':
# #         diseaseType = DiseaseType.objects.all()
# #         diseaseType_serializer = DiseaseTypeSerializer(diseaseType,many=True)
# #         res = JsonResponse(diseaseType_serializer.data,safe=False)
# #         return res
# #     elif request.method=='POST':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseType_serializer=DiseaseTypeSerializer(data=diseaseType_data)
# #         if diseaseType_serializer.is_valid():
# #             diseaseType_serializer.save()
# #             return JsonResponse("Added successfully",safe=False)
# #         return JsonResponse("Failed to add", safe=False)
# #     elif request.method=='PUT':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseType=DiseaseType.objects.get(id=diseaseType_data['id'])
# #         diseaseType_serializer=DiseaseTypeSerializer(diseaseType,data=diseaseType_data)
# #         if diseaseType_serializer.is_valid():
# #             diseaseType_serializer.save()
# #             return JsonResponse("Updates successfully",safe=False)
# #         return JsonResponse("Failed to update", safe=False)
# #     elif request.method=='DELETE':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseType=DiseaseType.objects.get(id=diseaseType_data['id'])
# #         diseaseType.delete()
# #         return JsonResponse("Deleted successfully",safe=False)

# # @csrf_exempt
# # def diseaseTypeApi(request):


# #     if request.method=='GET':
# #         diseaseTypes = DiseaseType.objects.all()
# #         diseaseTypes_serializer=DiseaseTypeSerializer(diseaseTypes,many=True)
# #         return JsonResponse(diseaseTypes_serializer.data,safe=False)

# #     elif request.method=='POST':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseTypes_serializer=DiseaseTypeSerializer(data=diseaseType_data)
# #         if diseaseTypes_serializer.is_valid():
# #             diseaseTypes_serializer.save()
# #             return JsonResponse("Added Successfully",safe=False)
# #         return JsonResponse("Failed to Add",safe=False)

# #     elif request.method=='PUT':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseTypes=DiseaseType.objects.get(diseaseTypeId=diseaseType_data['diseaseTypeId'])
# #         diseaseTypes_serializer=DiseaseTypeSerializer(diseaseTypes,data=diseaseType_data)
# #         if diseaseTypes_serializer.is_valid():
# #             diseaseTypes_serializer.save()
# #             return JsonResponse("Updated Successfully",safe=False)
# #         return JsonResponse("Failed to Update")

# #     elif request.method=='DELETE':
# #         diseaseType_data=JSONParser().parse(request)
# #         diseaseType=DiseaseType.objects.get(diseaseTypeId=diseaseType_data['diseaseTypeId'])
# #         diseaseType.delete()
# #         return JsonResponse("Deleted Successfully",safe=False)




# @csrf_exempt
# def countryApi(request):
#     if request.method=='GET':
#         countries = Country.objects.all()
#         countries_serializer = CountrySerializer(countries,many=True)
#         return JsonResponse(countries_serializer.data,safe=False)

#     elif request.method=='POST':
#         country_data=JSONParser().parse(request)
#         country_serializer=CountrySerializer(data=country_data)
#         if country_serializer.is_valid():
#             country_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         country_data=JSONParser().parse(request)
#         country=Country.objects.get(cname=country_data['cname'])
#         countries_serializer=CountrySerializer(country,data=country_data)
#         if countries_serializer.is_valid():
#             countries_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update", safe=True)

#     elif request.method=='DELETE':
#         country_data=JSONParser().parse(request)
#         country=Country.objects.get(cname=country_data['cname'])
#         country.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def diseaseApi(request):
#     if request.method=='GET':
#         diseases = Disease.objects.all()
#         diseases_serializer = DiseaseSerializer(diseases,many=True)
#         return JsonResponse(diseases_serializer.data,safe=False)

#     elif request.method=='POST':
#         disease_data=JSONParser().parse(request)
#         disease_serializer=DiseaseSerializer(data=disease_data)
#         if disease_serializer.is_valid():
#             disease_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         disease_data=JSONParser().parse(request)
#         disease=Disease.objects.get(disease_code=disease_data['disease_code'])
#         disease_serializer=DiseaseSerializer(disease,data=disease_data)
#         if disease_serializer.is_valid():
#             disease_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update", safe=True)

#     elif request.method=='DELETE':
#         disease_data=JSONParser().parse(request)
#         disease=Disease.objects.get(disease_code=disease_data['disease_code'])
#         disease.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def discoverApi(request):
#     if request.method=='GET':
#         discovers = Discover.objects.all()
#         discovers_serializer = DiscoverSerializer(discovers,many=True)
#         return JsonResponse(discovers_serializer.data,safe=False)

#     elif request.method=='POST':
#         discover_data=JSONParser().parse(request)
#         discover_serializer=DiscoverSerializer(data=discover_data)
#         if discover_serializer.is_valid():
#             discover_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         discover_data=JSONParser().parse(request)
#         discover=Discover.objects.get(cname=discover_data['cname'])
#         discover_serializer=DiscoverSerializer(discover,data=discover_data)
#         if discover_serializer.is_valid():
#             discover_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update", safe=True)

#     elif request.method=='DELETE':
#         discover_data=JSONParser().parse(request)
#         discover=Discover.objects.get(cname=discover_data['cname'])
#         discover.delete()
#         return JsonResponse("Deleted Successfully",safe=False)
    
# @csrf_exempt
# def usersApi(request):
#     if request.method=='GET':
#         users = Country.objects.all()
#         users_serializer = CountrySerializer(users,many=True)
#         return JsonResponse(users_serializer.data,safe=False)

#     elif request.method=='POST':
#         user_data=JSONParser().parse(request)
#         user_serializer=CountrySerializer(data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         user_data=JSONParser().parse(request)
#         user=Country.objects.get(email=user_data['email'])
#         user_serializer=CountrySerializer(user,data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update", safe=True)

#     elif request.method=='DELETE':
#         user_data=JSONParser().parse(request)
#         user=Country.objects.get(email=user_data['email'])
#         user.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def publicServantApi(request):
#     if request.method=='GET':
#         publicServants = PublicServant.objects.all()
#         publicServants_serializer = PublicServantSerializer(publicServants,many=True)
#         return JsonResponse(publicServants_serializer.data,safe=False)

#     elif request.method=='POST':
#         publicServant_data=JSONParser().parse(request)
#         publicServant_serializer=PublicServantSerializer(data=publicServant_data)
#         if publicServant_serializer.is_valid():
#             publicServant_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         publicServant_data=JSONParser().parse(request)
#         publicServant=PublicServant.objects.get(email=publicServant_data['email'])
#         publicServants_serializer=PublicServantSerializer(publicServant,data=publicServant_data)
#         if publicServants_serializer.is_valid():
#             publicServants_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update", safe=True)

#     elif request.method=='DELETE':
#         publicServant_data=JSONParser().parse(request)
#         publicServant=PublicServant.objects.get(email=publicServant_data['email'])
#         publicServant.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def doctorApi(request):
#     if request.method=='GET':
#         doctors = Doctor.objects.all()
#         doctors_serializer = DoctorSerializer(doctors,many=True)
#         return JsonResponse(doctors_serializer.data,safe=False)

#     elif request.method=='POST':
#         doctor_data=JSONParser().parse(request)
#         doctor_serializer=DoctorSerializer(data=doctor_data)
#         if doctor_serializer.is_valid():
#             doctor_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         doctor_data=JSONParser().parse(request)
#         doctor=Doctor.objects.get(email=doctor_data['email'])
#         doctors_serializer=DoctorSerializer(doctor,data=doctor_data)
#         if doctors_serializer.is_valid():
#             doctors_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update", safe=True)

#     elif request.method=='DELETE':
#         doctor_data=JSONParser().parse(request)
#         doctor=Doctor.objects.get(email=doctor_data['email'])
#         doctor.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def specializeApi(request):
#     if request.method=='GET':
#         specializes = Specialize.objects.all()
#         specializes_serializer = SpecializeSerializer(specializes,many=True)
#         return JsonResponse(specializes_serializer.data,safe=False)

#     elif request.method=='POST':
#         specialize_data=JSONParser().parse(request)
#         specialize_serializer=SpecializeSerializer(data=specialize_data)
#         if specialize_serializer.is_valid():
#             specialize_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         specialize_data=JSONParser().parse(request)
#         specialize=Specialize.objects.get(diseaseTypeId=specialize_data['diseaseTypeId'])
#         specializes_serializer=SpecializeSerializer(specialize,data=specialize_data)
#         if specializes_serializer.is_valid():
#             specializes_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update", safe=True)

#     elif request.method=='DELETE':
#         specialize_data=JSONParser().parse(request)
#         specialize=Specialize.objects.get(diseaseTypeId=specialize_data['diseaseTypeId'])
#         specialize.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def recordApi(request):
#     if request.method=='GET':
#         records = Record.objects.all()
#         records_serializer = RecordSerializer(records,many=True)
#         return JsonResponse(records_serializer.data,safe=False)

#     elif request.method=='POST':
#         record_data=JSONParser().parse(request)
#         record_serializer=RecordSerializer(data=record_data)
#         if record_serializer.is_valid():
#             record_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         record_data=JSONParser().parse(request)
#         record=Record.objects.get(email=record_data['email'])
#         records_serializer=RecordSerializer(record,data=record_data)
#         if records_serializer.is_valid():
#             records_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update", safe=True)

#     elif request.method=='DELETE':
#         record_data=JSONParser().parse(request)
#         record=Record.objects.get(email=record_data['email'])
#         record.delete()
#         return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def diseaseApi(request):
    if request.method=='GET':
        disease = Disease.objects.all()
        disease_serializer = DiseaseSerializer(disease,many=True)
        res = JsonResponse(disease_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        disease_data=JSONParser().parse(request)
        disease_serializer=DiseaseSerializer(data=disease_data)
        if disease_serializer.is_valid():
            disease_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        disease_data=JSONParser().parse(request)
        disease=Disease.objects.get(disease_code=disease_data['disease_code'])
        disease_serializer=DiseaseSerializer(disease,data=disease_data)
        if disease_serializer.is_valid():
            disease_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        disease_data=JSONParser().parse(request)
        disease=Disease.objects.get(disease_code=disease_data['disease_code'])
        disease.delete()
        return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def diseaseTypeApi(request):
    if request.method=='GET':
        diseaseType = DiseaseType.objects.all()
        diseaseType_serializer = DiseaseTypeSerializer(diseaseType,many=True)
        res = JsonResponse(diseaseType_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        diseaseType_data=JSONParser().parse(request)
        diseaseType_serializer=DiseaseTypeSerializer(data=diseaseType_data)
        if diseaseType_serializer.is_valid():
            diseaseType_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        diseaseType_data=JSONParser().parse(request)
        diseaseType=DiseaseType.objects.get(id=diseaseType_data['id'])
        diseaseType_serializer=DiseaseTypeSerializer(diseaseType,data=diseaseType_data)
        if diseaseType_serializer.is_valid():
            diseaseType_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        diseaseType_data=JSONParser().parse(request)
        diseaseType=DiseaseType.objects.get(id=diseaseType_data['id'])
        diseaseType.delete()
        return JsonResponse("Deleted successfully",safe=False)


@csrf_exempt
def countryApi(request):
    if request.method=='GET':
        country = Country.objects.all()
        country_serializer = CountrySerializer(country,many=True)
        res = JsonResponse(country_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        country_data=JSONParser().parse(request)
        country_serializer=CountrySerializer(data=country_data)
        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        country_data=JSONParser().parse(request)
        country=Country.objects.get(cname=country_data['cname'])
        country_serializer=CountrySerializer(country,data=country_data)
        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        country_data=JSONParser().parse(request)
        country=Country.objects.get(cname=country_data['cname'])
        country.delete()
        return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def discoverApi(request):
    if request.method=='GET':
        discover = Discover.objects.all()
        discover_serializer = DiscoverSerializer(discover,many=True)
        res = JsonResponse(discover_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        discover_data=JSONParser().parse(request)
        discover_serializer=DiscoverSerializer(data=discover_data)
        if discover_serializer.is_valid():
            discover_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        discover_data=JSONParser().parse(request)
        discover=Discover.objects.get(cname=discover_data['cname'], disease_code=discover_data['disease_code'])
        discover_serializer=DiscoverSerializer(discover,data=discover_data)
        if discover_serializer.is_valid():
            discover_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        discover_data=JSONParser().parse(request)
        discover=Discover.objects.get(cname=discover_data['cname'])
        discover.delete()
        return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def usersApi(request):
    if request.method=='GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users,many=True)
        res = JsonResponse(users_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        users_data=JSONParser().parse(request)
        users_serializer=UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        users_data=JSONParser().parse(request)
        users=Users.objects.get(email=users_data['email'])
        users_serializer=UsersSerializer(users,data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        users_data=JSONParser().parse(request)
        users=Users.objects.get(email=users_data['email'])
        users.delete()
        return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def publicServantApi(request):
    if request.method=='GET':
        publicServant = PublicServant.objects.all()
        publicServant_serializer = PublicServantSerializer(publicServant,many=True)
        res = JsonResponse(publicServant_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        publicServant_data=JSONParser().parse(request)
        publicServant_serializer=PublicServantSerializer(data=publicServant_data)
        if publicServant_serializer.is_valid():
            publicServant_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        publicServant_data=JSONParser().parse(request)
        publicServant=PublicServant.objects.get(email=publicServant_data['email'])
        publicServant_serializer=PublicServantSerializer(publicServant,data=publicServant_data)
        if publicServant_serializer.is_valid():
            publicServant_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        publicServant_data=JSONParser().parse(request)
        publicServant=PublicServant.objects.get(email=publicServant_data['email'])
        publicServant.delete()
        return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def doctorApi(request):
    if request.method=='GET':
        doctor = Doctor.objects.all()
        doctor_serializer = DoctorSerializer(doctor,many=True)
        res = JsonResponse(doctor_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        doctor_data=JSONParser().parse(request)
        doctor_serializer=DoctorSerializer(data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        doctor_data=JSONParser().parse(request)
        doctor=Doctor.objects.get(email=doctor_data['email'])
        doctor_serializer=DoctorSerializer(doctor,data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        doctor_data=JSONParser().parse(request)
        doctor=Doctor.objects.get(email=doctor_data['email'])
        doctor.delete()
        return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def specializeApi(request):
    if request.method=='GET':
        specialize = Specialize.objects.all()
        specialize_serializer = SpecializeSerializer(specialize,many=True)
        res = JsonResponse(specialize_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        specialize_data=JSONParser().parse(request)
        specialize_serializer=SpecializeSerializer(data=specialize_data)
        if specialize_serializer.is_valid():
            specialize_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        specialize_data=JSONParser().parse(request)
        specialize=Specialize.objects.get(diseaseid=specialize_data['diseaseid'], email=specialize_data['email'])
        specialize_serializer=SpecializeSerializer(specialize,data=specialize_data)
        if specialize_serializer.is_valid():
            specialize_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        specialize_data=JSONParser().parse(request)
        specialize=Specialize.objects.get(diseaseid=specialize_data['diseaseid'], email=specialize_data['email'])
        specialize.delete()
        return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def recordApi(request):
    if request.method=='GET':
        record = Record.objects.all()
        record_serializer = RecordSerializer(record,many=True)
        res = JsonResponse(record_serializer.data,safe=False)
        return res
    elif request.method=='POST':
        record_data=JSONParser().parse(request)
        record_serializer=RecordSerializer(data=record_data)
        if record_serializer.is_valid():
            record_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        record_data=JSONParser().parse(request)
        record=Record.objects.get(cname=record_data['cname'], email=record_data['email'], disease_code=record_data['disease_code'])
        record_serializer=RecordSerializer(record,data=record_data)
        if record_serializer.is_valid():
            record_serializer.save()
            return JsonResponse("Updates successfully",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        record_data=JSONParser().parse(request)
        record=Record.objects.get(cname=record_data['cname'], email=record_data['email'], disease_code=record_data['disease_code'])
        record.delete()
        return JsonResponse("Deleted successfully",safe=False)

engine = create_engine('postgresql://postgres:budT4alEoPMiruDRmCuW@containers-us-west-128.railway.app:6076/railway', echo=False)

@csrf_exempt
def query01Api(request):
    if request.method=='GET':
        sql = text(
            '''
                SELECT disease.disease_code, disease.description
                FROM disease INNER JOIN discover
                ON disease.disease_code = discover.disease_code
                WHERE pathogen = 'bacteria' AND first_enc_date < '1990-01-01';
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res

    
@csrf_exempt
def query02Api(request):
    if request.method=='GET':
        sql = text(
            '''
                SELECT users.name, users.surname, doctor.degree
                FROM users
                INNER JOIN doctor  ON users.email = doctor.email
                WHERE doctor.email NOT IN (
                    SELECT specialize.email
                    FROM specialize
                    INNER JOIN diseasetype ON specialize.id = diseasetype.id
                    WHERE diseasetype.description = 'infectious');
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res
    
@csrf_exempt
def query03Api(request):
    if request.method=='GET':
        sql = text(
            '''

                SELECT DISTINCT U.name, U.surname, D.degree
                FROM users U, doctor D, specialize S
                WHERE U.email = D.email AND D.email IN(
                SELECT S.email
                FROM specialize S
                INNER JOIN diseasetype dt ON S.id = dt.id
                GROUP BY S.email
                HAVING COUNT(*) >=2);
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res

@csrf_exempt
def query04Api(request):
    if request.method=='GET':
        sql = text(
            '''
                SELECT country.cname, AVG(users.salary)
                    FROM country INNER JOIN users
                    ON country.cname = users.cname
                    INNER JOIN specialize
                    ON users.email = specialize.email
                    INNER JOIN diseasetype
                    ON specialize.id = diseasetype.id
                    WHERE specialize.id IN (
                        SELECT diseasetype.id
                        FROM diseasetype
                        WHERE diseasetype.description = 'virology')
                    GROUP BY country.cname;
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res
    

@csrf_exempt
def query05Api(request):
    if request.method=='GET':
        sql = text(
            '''
                SELECT publicServant.department, COUNT(*)
                FROM publicServant
                WHERE publicServant.email IN (
                    SELECT DISTINCT record.email
                    FROM record
                    WHERE record.disease_code = 'covid-19'
                    GROUP BY record.email
                    HAVING COUNT(*) > 1)
                GROUP BY publicServant.department;
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res
    

@csrf_exempt
def query06Api(request):
    if request.method=='GET':
        sql = text(
            '''
                UPDATE users 
                SET salary = salary * 2
                WHERE email IN(
                    SELECT r.email
                    FROM record r
                    WHERE r.disease_code = 'covid-19'
                    GROUP BY r.email
                    HAVING COUNT(*) > 3
                    );
                    SELECT * FROM users;
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res
    

@csrf_exempt
def query07Api(request):
    if request.method=='GET':
        sql = text(
            '''
                DELETE FROM users
                WHERE name LIKE '%%bek%%' 
                OR name LIKE '%%gul%%'
                OR name LIKE '%%Gul%%'
                OR name LIKE '%%Bek%%';
                SELECT * FROM users;
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res
    

@csrf_exempt
def query08Api(request):
    if request.method=='GET':
        sql = text(
            '''
                CREATE INDEX "idx_pathogen"
                ON  disease(pathogen);
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res
    
@csrf_exempt
def query09Api(request):
    if request.method=='GET':
        sql = text(
            '''
                SELECT users.email, users.name, publicservant.department
                FROM users
                INNER JOIN publicservant
                ON users.email = publicservant.email
                INNER JOIN record
                ON publicservant.email = record.email
                WHERE record.total_patients > 100000 and record.total_patients <999999
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res


@csrf_exempt
def query10Api(request):
    if request.method=='GET':
        sql = text(
            '''
                SELECT cname, sum(total_patients)
                    FROM record
                    group by cname
                    ORDER BY sum(total_patients) DESC
                    LIMIT 5;
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res
    
@csrf_exempt
def query11Api(request):
    if request.method=='GET':
        sql = text(
            '''
            SELECT diseasetype.description, sum(record.total_patients)
                FROM diseasetype
                left join disease
                on diseasetype.id = disease.id
                left join record
                on disease.disease_code = record.disease_code
                group by (diseasetype.description);
            ''')
        res = engine.connect().execute(sql).fetchall()
        return res
    