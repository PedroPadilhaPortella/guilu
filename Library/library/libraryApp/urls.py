from django.urls import path
from libraryApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register')
]