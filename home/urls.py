from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_redirect),  
    path('home/', views.book_appointment, name='home'),
    path('ajax/slot-availability/', views.slot_availability, name='slot_availability'),
    path('success/', views.booking_success, name='success'),
]
