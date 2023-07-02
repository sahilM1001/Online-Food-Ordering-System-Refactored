from django.urls import path
from . import views

urlpatterns=[
    path('', views.loginPage, name='Login'),
    path('login', views.login, name='Login API'),
    path('signup', views.signupPage, name='SignUp'),
    path('home', views.indexFunc, name='Home Page'),
    path('adminHome', views.adminHome, name='Admin Home'),
    path('restaurantHome', views.restaurantHome, name='Restaurant Home')
]