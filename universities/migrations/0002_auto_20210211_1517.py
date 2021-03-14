# Generated by Django 3.1.3 on 2021-02-11 09:47

from django.db import migrations, models
import django.db.models.deletion
import universities.models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_enroll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.universities_course', verbose_name='Enroll Course Name'),
        ),
        migrations.AlterField(
            model_name='universities_course',
            name='fees',
            field=models.IntegerField(validators=[universities.models.validate_fees], verbose_name='Course fees'),
        ),
        migrations.AlterField(
            model_name='university',
            name='uni_id',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[universities.models.validate_id]),
        ),
    ]
