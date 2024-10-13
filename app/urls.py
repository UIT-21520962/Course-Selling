from django.contrib import admin
from django.urls import path
from .views import register_course
from . import views
urlpatterns = [
    path('', views.home),
    path('AllCourses', views.Allcourse),
    path('base', views.home, name = 'base'),
    path('home', views.home, name = 'home'),
    path('CourseDetails', views.CourseDetails),
    path('MyCourses', views.MyCourse ),
    path('register_course/', register_course, name='register_course'),
    path('LoginForm', views.LoginForm),
    path('LoginForm', views.LoginForm, name='login'),
    path('RegisterForm', views.RegisterForm, name='register'),

]
