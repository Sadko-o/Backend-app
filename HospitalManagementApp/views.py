from django.core.files.storage import default_storage
from sqlalchemy import create_engine
from sqlalchemy import text
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from HospitalManagementApp.models import *
from HospitalManagementApp.serializers import *
import simplejson
from django.db import connection

engine = create_engine('postgresql://postgres:ZDPPgZRMqYytPKqutZms@containers-us-west-36.railway.app:5832/railway', echo=False)

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
            return JsonResponse("Added",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        diseaseType_data=JSONParser().parse(request)
        diseaseType=DiseaseType.objects.get(id=diseaseType_data['id'])
        diseaseType_serializer=DiseaseTypeSerializer(diseaseType,data=diseaseType_data)
        if diseaseType_serializer.is_valid():
            diseaseType_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        diseaseType_data=JSONParser().parse(request)
        diseaseType=DiseaseType.objects.get(id=diseaseType_data['id'])
        diseaseType.delete()
        return JsonResponse("Deleted",safe=False)

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
            return JsonResponse("Added ",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        disease_data=JSONParser().parse(request)
        disease=Disease.objects.get(disease_code=disease_data['disease_code'])
        disease_serializer=DiseaseSerializer(disease,data=disease_data)
        if disease_serializer.is_valid():
            disease_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        disease_data=JSONParser().parse(request)
        disease=Disease.objects.get(disease_code=disease_data['disease_code'])
        disease.delete()
        return JsonResponse("Deleted ",safe=False)




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
            return JsonResponse("Added ",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        country_data=JSONParser().parse(request)
        country=Country.objects.get(cname=country_data['cname'])
        country_serializer=CountrySerializer(country,data=country_data)
        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        country_data=JSONParser().parse(request)
        country=Country.objects.get(cname=country_data['cname'])
        country.delete()
        return JsonResponse("Deleted ",safe=False)

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
            return JsonResponse("Added ",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        discover_data=JSONParser().parse(request)
        discover=Discover.objects.get(cname=discover_data['cname'], disease_code=discover_data['disease_code'])
        discover_serializer=DiscoverSerializer(discover,data=discover_data)
        if discover_serializer.is_valid():
            discover_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        discover_data=JSONParser().parse(request)
        discover=Discover.objects.get(cname=discover_data['cname'])
        discover.delete()
        return JsonResponse("Deleted ",safe=False)

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
            return JsonResponse("Added ",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        users_data=JSONParser().parse(request)
        users=Users.objects.get(email=users_data['email'])
        users_serializer=UsersSerializer(users,data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        users_data=JSONParser().parse(request)
        users=Users.objects.get(email=users_data['email'])
        users.delete()
        return JsonResponse("Deleted ",safe=False)

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
            return JsonResponse("Added ",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        publicServant_data=JSONParser().parse(request)
        publicServant=PublicServant.objects.get(email=publicServant_data['email'])
        publicServant_serializer=PublicServantSerializer(publicServant,data=publicServant_data)
        if publicServant_serializer.is_valid():
            publicServant_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        publicServant_data=JSONParser().parse(request)
        publicServant=PublicServant.objects.get(email=publicServant_data['email'])
        publicServant.delete()
        return JsonResponse("Deleted ",safe=False)

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
            return JsonResponse("Added ",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        doctor_data=JSONParser().parse(request)
        doctor=Doctor.objects.get(email=doctor_data['email'])
        doctor_serializer=DoctorSerializer(doctor,data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        doctor_data=JSONParser().parse(request)
        doctor=Doctor.objects.get(email=doctor_data['email'])
        doctor.delete()
        return JsonResponse("Deleted ",safe=False)

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
            return JsonResponse("Added ",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        specialize_data=JSONParser().parse(request)
        specialize=Specialize.objects.get(diseaseid=specialize_data['diseaseid'], email=specialize_data['email'])
        specialize_serializer=SpecializeSerializer(specialize,data=specialize_data)
        if specialize_serializer.is_valid():
            specialize_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        specialize_data=JSONParser().parse(request)
        specialize=Specialize.objects.get(diseaseid=specialize_data['diseaseid'], email=specialize_data['email'])
        specialize.delete()
        return JsonResponse("Deleted ",safe=False)

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
            return JsonResponse("Added ",safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        record_data=JSONParser().parse(request)
        record=Record.objects.get(cname=record_data['cname'], email=record_data['email'], disease_code=record_data['disease_code'])
        record_serializer=RecordSerializer(record,data=record_data)
        if record_serializer.is_valid():
            record_serializer.save()
            return JsonResponse("Updates ",safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        record_data=JSONParser().parse(request)
        record=Record.objects.get(cname=record_data['cname'], email=record_data['email'], disease_code=record_data['disease_code'])
        record.delete()
        return JsonResponse("Deleted ",safe=False)


@csrf_exempt
def query01Api(request):
    with connection.cursor() as cursor:
        sql = 'SELECT DISTINCT disease_code, description FROM "HospitalManagementApp_disease"  INNER JOIN "HospitalManagementApp_discover"  ON disease_code = disease_code WHERE pathogen = {pathogen} AND first_enc_date < {date}'.format(pathogen = "'bacteria'", date =  "'1990-01-01'")
        cursor.execute(sql)
        return HttpResponse(
            simplejson.dumps(cursor.fetchall(), use_decimal = True))


# @csrf_exempt
# def query1(request):
#     with connection.cursor() as cursor:
#         # List the disease code and the description of diseases that are caused by “bacteria” (pathogen) and were discovered before 1990
#         q = 'SELECT "Disease"."disease code", description FROM "Disease" INNER JOIN "Discover" ON "Disease"."disease code" = "Discover"."disease code" WHERE "Disease".pathogen = {pathogen} AND "Discover"."first enc date" < {date}'.format(pathogen = "'bacteria'", date = "'1990-1-1'")
#         cursor.execute(q)
#         return HttpResponse(
#         simplejson.dumps(dictfetchall(cursor)),
#         content_type = 'application/javascript; charset=utf8'
#     )

    
# @csrf_exempt
# def query02Api(request):
#     if request.method=='GET':
#         sql = text(
#             '''
#                 SELECT DISTINCT  "HospitalManagementApp_users".name, "HospitalManagementApp_users".surname, "HospitalManagementApp_doctor".degree
#                 FROM "HospitalManagementApp_users"
#                 INNER JOIN  "HospitalManagementApp_doctor"  
#                 ON "HospitalManagementApp_users".email = "HospitalManagementApp_doctor".email_id
#                 WHERE "HospitalManagementApp_doctor".email_id NOT IN (
#                                     SELECT DISTINCT email
#                                     FROM "HospitalManagementApp_specialize"
#                                     INNER JOIN "HospitalManagementApp_diseasetype" ON "HospitalManagementApp_specialize".diseaseid_id= "HospitalManagementApp_diseasetype".id
#                                     WHERE "HospitalManagementApp_diseasetype".description = 'infectious');
#             ''')
#         res = engine.connect().execute(sql).fetchall()
#         return res
    
# @csrf_exempt
# def query03Api(request):
#     if request.method=='GET':
#         sql = text(
#             '''
#                 SELECT DISTINCT "HospitalManagementApp_users".name, "HospitalManagementApp_users".surname, "HospitalManagementApp_doctor".degree
#                 FROM "HospitalManagementApp_users", "HospitalManagementApp_doctor", "HospitalManagementApp_specialize"
#                 WHERE "HospitalManagementApp_users".email = "HospitalManagementApp_doctor".email_id AND "HospitalManagementApp_doctor".email_id IN(
#                 SELECT "HospitalManagementApp_specialize".email_id
#                 FROM "HospitalManagementApp_specialize"
#                 INNER JOIN "HospitalManagementApp_diseasetype" ON "HospitalManagementApp_specialize".id = "HospitalManagementApp_diseasetype".id
#                 GROUP BY "HospitalManagementApp_specialize".email_id
#                 HAVING COUNT(*) >=2);
#             ''')
#         res = engine.connect().execute(sql).fetchall()
#         return res

# @csrf_exempt
# def query04Api(request):
#     if request.method=='GET':
#         sql = text(
#             '''
#                     SELECT "HospitalManagementApp_country".cname, AVG("HospitalManagementApp_users".salary)
#                     FROM "HospitalManagementApp_country" 
#                     INNER JOIN "HospitalManagementApp_users"
#                     ON "HospitalManagementApp_country".cname = "HospitalManagementApp_users".cname_id
#                     INNER JOIN "HospitalManagementApp_specialize"
#                     ON "HospitalManagementApp_users".email = "HospitalManagementApp_specialize".email_id
#                     INNER JOIN "HospitalManagementApp_diseasetype"
#                     ON "HospitalManagementApp_specialize".diseaseid_id = "HospitalManagementApp_diseasetype".id
#                     WHERE "HospitalManagementApp_specialize".diseaseid_id IN (
#                         SELECT "HospitalManagementApp_diseasetype".id
#                         FROM "HospitalManagementApp_diseasetype"
#                         WHERE "HospitalManagementApp_diseasetype".description = 'virology')
#                     GROUP BY "HospitalManagementApp_country".cname;
#             ''')
#         res = engine.connect().execute(sql).fetchall()
#         return res
    

# @csrf_exempt
# def query05Api(request):
#     if request.method=='GET':
#         sql = text(
#             '''
#                 SELECT "HospitalManagementApp_publicservant".department, COUNT(*)
#                 FROM "HospitalManagementApp_publicservant"
#                 WHERE "HospitalManagementApp_publicservant".email_id IN (
#                     SELECT DISTINCT "HospitalManagementApp_record".email_id
#                     FROM "HospitalManagementApp_record"
#                     WHERE "HospitalManagementApp_record".disease_code_id = 'covid-19'
#                     GROUP BY "HospitalManagementApp_record".email_id
#                     HAVING COUNT(*) > 1)
#                 GROUP BY "HospitalManagementApp_publicservant".department;
#             ''')
#         res = engine.connect().execute(sql).fetchall()
#         return res
    

# # @csrf_exempt
# # def query06Api(request):
# #     if request.method=='GET':
# #         sql = text(
# #             '''
#                 # UPDATE users 
#                 # SET salary = salary * 2
#                 # WHERE email IN(
#                 #     SELECT r.email
#                 #     FROM record r
#                 #     WHERE r.disease_code = 'covid-19'
#                 #     GROUP BY r.email
#                 #     HAVING COUNT(*) > 3
#                 #     );
#                 #     SELECT * FROM users;
# #             ''')
# #         res = engine.connect().execute(sql).fetchall()
# #         return res
    

# @csrf_exempt
# def query07Api(request):
#     if request.method=='GET':
#         sql = text(
#             # delete 
#             '''
#     SELECT  * FROM "HospitalManagementApp_users"
#                 WHERE name LIKE '%%bek%%' 
#                 OR name LIKE '%%gul%%'
#                 OR name LIKE '%%Gul%%'
#                 OR name LIKE '%%Bek%%';
               
#             ''')
#         res = engine.connect().execute(sql).fetchall()
#         return res
    

# # @csrf_exempt
# # def query08Api(request):
# #     if request.method=='GET':
# #         sql = text(
# #             '''
# #                 CREATE INDEX "idx_pathogen"
# #                 ON  disease(pathogen);
# #             ''')
# #         res = engine.connect().execute(sql).fetchall()
# #         return res
    
# @csrf_exempt
# def query09Api(request):
#     if request.method=='GET':
#         sql = text(
#             '''
#                 SELECT "HospitalManagementApp_users".email, "HospitalManagementApp_users".name, "HospitalManagementApp_publicservant".department
#                 FROM "HospitalManagementApp_users"
#                 INNER JOIN "HospitalManagementApp_publicservant"
#                 ON "HospitalManagementApp_users".email = "HospitalManagementApp_publicservant".email_id
#                 INNER JOIN "HospitalManagementApp_record"
#                 ON "HospitalManagementApp_publicservant".email_id = "HospitalManagementApp_record".email_id
#                 WHERE "HospitalManagementApp_record".total_patients > 100000 and "HospitalManagementApp_record".total_patients <999999
#             ''')
#         res = engine.connect().execute(sql).fetchall()
#         return res


# @csrf_exempt
# def query10Api(request):
#     if request.method=='GET':
#         sql = text(
#             '''
#                 SELECT "HospitalManagementApp_record".cname_id, SUM("HospitalManagementApp_record".total_patients)
#                     FROM "HospitalManagementApp_record"
#                     GROUP BY  "HospitalManagementApp_record".cname_id
#                     ORDER BY SUM("HospitalManagementApp_record".total_patients) DESC
#                     LIMIT 5;
#             ''')
#         res = engine.connect().execute(sql).fetchall()
#         return res
    
# @csrf_exempt
# def query11Api(request):
#     if request.method=='GET':
#         sql = text(
#             '''
#           SELECT  "HospitalManagementApp_diseasetype".description, SUM("HospitalManagementApp_record".total_patients)
#                 FROM "HospitalManagementApp_diseasetype"
#                 LEFT JOIN "HospitalManagementApp_disease"
#                 ON "HospitalManagementApp_diseasetype".id = "HospitalManagementApp_disease".id_id
#                 LEFT JOIN "HospitalManagementApp_record"
#                 ON "HospitalManagementApp_disease".disease_code = "HospitalManagementApp_record".disease_code_id
#                 GROUP BY ("HospitalManagementApp_diseasetype".description);
#             ''')
#         res = engine.connect().execute(sql).fetchall()
#         return res
    