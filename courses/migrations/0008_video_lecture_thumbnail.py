# Generated by Django 3.1.3 on 2021-02-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20210204_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_lecture',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='video_lectures/thubnails'),
        ),
    ]