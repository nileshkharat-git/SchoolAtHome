from django.urls import path
from . import views
urlpatterns=[
    path('lecture+list/<uni_course>',views.display_lecture,name='display_lecture'),
    path('display_list/',views.university_apply,name='universities'),
    path('payment/<int:course_id>',views.payment,name='payment'),
    path('payment/proceed',views.proceed_payment,name='proceed'),
    path('login_warn/',views.login_message),
    path('lecture-play/<int:lec_id>/',views.lecture_play,name='lecture_play'),


]