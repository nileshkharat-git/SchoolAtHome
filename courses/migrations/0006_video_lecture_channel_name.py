# Generated by Django 3.1.3 on 2021-02-03 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_video_lecture_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_lecture',
            name='channel_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.channel_details'),
        ),
    ]
