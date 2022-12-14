# Generated by Django 3.2.16 on 2022-11-23 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HospitalManagementApp', '0002_auto_20221123_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('population', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagementApp.country')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='HospitalManagementApp.users')),
                ('degree', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PublicServant',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='HospitalManagementApp.users')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=140)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagementApp.diseasetype')),
            ],
        ),
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseaseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagementApp.diseasetype')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagementApp.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_deaths', models.IntegerField()),
                ('total_patients', models.IntegerField()),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagementApp.country')),
                ('disease_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagementApp.disease')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagementApp.publicservant')),
            ],
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('cname', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='HospitalManagementApp.country')),
                ('first_enc_date', models.DateField()),
                ('disease_code', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='HospitalManagementApp.disease')),
            ],
        ),
    ]
