from django.urls import path
from . import views

urlpatterns = [
    path('genders/', views.list_genders, name='list_genders'),
    path('gender/add/', views.add_gender, name='add_gender'),
]
