from django.contrib import admin
from .models import Course_Type,Channel_Details,Video_lecture

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_type_name']

class Channel_Admin(admin.ModelAdmin):
    list_display = ['channel_name','channel_owner','channel_type']

class Video_Admin(admin.ModelAdmin):
    list_display = ['vid','name_of_video','uploaded_on','details']

admin.site.register(Course_Type,CourseAdmin)
admin.site.register(Channel_Details,Channel_Admin)
admin.site.register(Video_lecture,Video_Admin)