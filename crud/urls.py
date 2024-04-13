from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.list_genders, name='list_genders'),
    path('gender/add', views.add_gender, name='add_gender'),
    path('gender/store', views.store_gender, name='store_gender'),
    path('gender/view/<int:id>', views.view_gender, name='view_gender'),
]
