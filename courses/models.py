from django.db import models
from accounts.models import Accounts
class Course_Type(models.Model):
    course_type_name=models.CharField(max_length=255,verbose_name="Course Type")

    def __str__(self):
        return self.course_type_name

class Channel_Details(models.Model):
    channel_name=models.CharField(max_length=255,verbose_name="Channel name",unique=True)
    channel_owner=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    channel_type=models.ForeignKey(Course_Type,on_delete=models.CASCADE)
    channel_logo=models.ImageField(blank=True,null=True,upload_to='channel_logo/')

    def __str__(self):
        return self.channel_name

class Video_lecture(models.Model):
    vid=models.AutoField(primary_key=True)
    channel_name=models.ForeignKey(Channel_Details,on_delete=models.CASCADE,null=True)
    name_of_video=models.CharField(max_length=255,verbose_name="Video Title")
    uploaded_on=models.DateField(auto_now_add=True,verbose_name="Uploaded On")
    details=models.TextField(max_length=500,verbose_name="Details")
    video=models.FileField(blank=True,null=True,verbose_name="Video", upload_to='video_lectures/')
    thumbnail=models.ImageField(blank=True,null=True,upload_to='video_lectures/thubnails')