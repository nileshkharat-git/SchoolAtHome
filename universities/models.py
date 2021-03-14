from django.db import models
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from accounts.models import Accounts

def validate_id(uni_id):
    if uni_id>=100000 and uni_id<=999999:
        return True
    else:
        raise ValidationError('Invalid ID!')


class University(models.Model):
    uni_id=models.IntegerField(primary_key=True,validators=[validate_id])
    uni_name=models.CharField(max_length=200,verbose_name="University Name",unique=True)
    country=CountryField(blank=False)

    def __str__(self):
        return self.uni_name

def validate_fees(fees):
    if fees<=100000:
        return True
    else:
        raise ValidationError("You can't take this much of amount as fees!!")


class Universities_Course(models.Model):
    course_offered = models.CharField(max_length=250, verbose_name="Course Name")
    university=models.ForeignKey(University,verbose_name="University",on_delete=models.CASCADE)
    fees = models.IntegerField(verbose_name="Course fees",validators=[validate_fees])
    duration=models.IntegerField(verbose_name="Duration of Course(in days)",null=True)
    def __str__(self):
        return f"{self.university}--{self.course_offered}"

def set_lecture_url(instance,filename):
    return f"university_lectures/{instance.university_course.university.uni_name}/{instance.university_course.course_offered}/{filename}"

def set_lecture_thumdnail_url(instance,filename):
    return f"university_lectures/{instance.university_course.university.uni_name}/" \
           f"{instance.university_course.course_offered}/thumbnails/{filename}"


class Lecutures(models.Model):
    university_course=models.ForeignKey(Universities_Course,on_delete=models.CASCADE)
    lecture=models.FileField(blank=True,null=True,upload_to=set_lecture_url)
    thumbnail=models.ImageField(blank=True,null=True,upload_to=set_lecture_thumdnail_url)


    def __str__(self):
        return f"{self.university_course}"

class Student(models.Model):
    student=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    course_enroll=models.ForeignKey(Universities_Course,verbose_name="Enroll Course Name",on_delete=models.CASCADE)
    paid=models.BooleanField(default=False,verbose_name="Payment")

