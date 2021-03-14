from django.urls import path
from . import views
urlpatterns=[
    path('signup/',views.signUp, name='signUp'),
    path('login/',views.user_login,name='logIn'),
    path('dashboard/',views.user_dashboard,name='dashboard'),
    path('logout/',views.user_logout,name='logOut'),


]