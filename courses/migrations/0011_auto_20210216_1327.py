# Generated by Django 3.1.3 on 2021-02-16 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20210206_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel_details',
            name='channel_logo',
            field=models.ImageField(blank=True, null=True, upload_to='channel_logo/'),
        ),
        migrations.AlterField(
            model_name='video_lecture',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video_lectures/', verbose_name='Video'),
        ),
    ]
