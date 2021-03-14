# Generated by Django 3.1.3 on 2021-02-11 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('uni_id', models.IntegerField(primary_key=True, serialize=False)),
                ('uni_name', models.CharField(max_length=200, unique=True, verbose_name='University Name')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Universities_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_offered', models.CharField(max_length=250, verbose_name='Course Offered By University')),
                ('fees', models.IntegerField(verbose_name='Course fees')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.university', verbose_name='University')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_enroll', models.CharField(max_length=250, verbose_name='Enroll Course Name')),
                ('paid', models.BooleanField(default=False, verbose_name='Payment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
