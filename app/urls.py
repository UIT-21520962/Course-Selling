from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('AdvertisingBanner', views.products_view, name='AdvertisingBanner'),
     path('base', views.home_products, name='home'),  # Đường dẫn đến trang chủ
    path('Products', views.products_view, name = 'Products'),
    path('ProductOrders', views.ProductOrders, name = 'ProductOrders'),
    path('Products1', views.products1_view, name = 'Products1'),
    path('Products2', views.products2_view, name = 'Products2'),
    path('base', views.home, name = 'base'),
    path('home', views.home, name = 'home'),
    path('LoginForm', views.LoginForm, name='login'),
    path('RegisterForm', views.RegisterForm, name='register'),
    path('logout', views.logout_view, name = 'logout'),
    path('register', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('social-media', views.ProductOrders, name='social_media'),
]

