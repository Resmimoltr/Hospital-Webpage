from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('departments', views.department, name='dept'),
    path('doctors', views.doctors, name='doct'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='book'),
]
