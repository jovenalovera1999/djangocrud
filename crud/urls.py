from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.list_genders),
    path('gender/add', views.add_gender),
    path('gender/store', views.store_gender),
    path('gender/view/<int:id>', views.view_gender),
    path('gender/edit/<int:id>', views.edit_gender),
    path('gender/update/<int:id>', views.update_gender),
    path('gender/delete/<int:id>', views.delete_gender),
    path('gender/destroy/<int:id>', views.destroy_gender),
    path('users', views.list_users),
    path('user/add', views.add_user),
    path('user/store', views.store_user),
]
