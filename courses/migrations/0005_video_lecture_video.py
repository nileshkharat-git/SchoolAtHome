# Generated by Django 3.1.3 on 2021-02-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_video_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_lecture',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Video'),
        ),
    ]
