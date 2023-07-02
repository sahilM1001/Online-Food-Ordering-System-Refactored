from django.urls import path
from . import views

urlpatterns=[
    path('', views.foodlisting, name='Home'),
    path('/view-food', views.foodlisting, name='Food Item Management'),
    path('/view-orders', views.orderlisting, name='Order Management'),
    path('/view-delivery', views.deliverylisting, name='Delivery Management'),
    path('/view-feedback', views.feedbacklisting, name='Feedbacks Management'),
    path('/view-payment', views.paymentlisting, name='Payments Management'),

    path('/add-food', views.foodaddcreate, name='Food Item Management'),
    path('/logout', views.restaurantLogout, name='Restaurant Logout'),
    path('/inserted', views.foodaddprocess, name="Food Added"),

    path('/delete/<int:id>', views.foodDelete, name =  'Remove Food Item')
]