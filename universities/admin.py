from django.contrib import admin
from .models import *

class UniAdmin(admin.ModelAdmin):
    list_display = ['uni_id','uni_name','country']
admin.site.register(University,UniAdmin)

class UniCourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_offered','university','fees','duration']
admin.site.register(Universities_Course,UniCourseAdmin)

class LectureAdmin(admin.ModelAdmin):
    list_display = ['id','university_course','lecture']
admin.site.register(Lecutures,LectureAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student','course_enroll','paid']
admin.site.register(Student,StudentAdmin)

