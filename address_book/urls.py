from django.urls import path
from .views import *
from . import views

app_name = 'address_book'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_address/', views.add_address, name='add_address'),
    path('address_list/', AddressList.as_view(), name='address_list'),
]
