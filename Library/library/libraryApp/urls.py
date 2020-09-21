from django.urls import path
from libraryApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('edit_lib/<int:id>', views.EditLib.as_view(), name='edit_lib'),
    path('remove_lib/<int:id>', views.remove_lib, name='remove_lib')
]