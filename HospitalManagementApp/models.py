from django.db import models
import _datetime

class DiseaseType(models.Model):
    diseaseTypeId = models.IntegerField(primary_key=True)
    diseaseTypeDescription = models.CharField(max_length=140)

class Country(models.Model):
    cname = models.CharField(max_length=50, primary_key=True)
    population = models.BigIntegerField()

class Disease(models.Model):
    disease_code = models.CharField(max_length=50, primary_key=True)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    diseaseTypeId = models.ForeignKey(DiseaseType, default=None, on_delete=models.CASCADE)

class Discover(models.Model):
    cname = models.OneToOneField(Country, primary_key=True, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    first_enc_date = models.DateField(default= _datetime.datetime.now)

class Users(models.Model):
    email = models.CharField(max_length=60, unique=True,primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)

class PublicServant(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=50)

class Doctor(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE, primary_key=True)
    degree = models.CharField(max_length=20)

class Specialize(models.Model):
    diseaseTypeId = models.ForeignKey(DiseaseType, default=None, on_delete=models.CASCADE, primary_key=True)
    email = models.ForeignKey(Users, on_delete=models.CASCADE)

class Record(models.Model):
    email = models.ForeignKey(PublicServant, on_delete=models.CASCADE, primary_key=True)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField( blank=True, null=True)

