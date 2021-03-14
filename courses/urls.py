from django.urls import path
from . import views
urlpatterns=[
    path('menu/',views.courses,name='courses'),
    path('menu/videos_by_channel/<channel_id>',views.show_course_by_chanel ,name='show_video'),
    path('menu/videos_by_channel/<int:vid>/<channel_id>',views.show_course_by_chanel,name='req_video'),
    path('menu/login_warn/',views.login_message),
]