from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_redirect),  
    path('home/', views.book_appointment, name='home'),
    path('success/<uuid:booking_id>/', views.booking_success, name='success'),
]
