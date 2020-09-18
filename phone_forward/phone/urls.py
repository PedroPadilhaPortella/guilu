from django.urls import path
import phone.views as views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('registered', views.registered_func, name='registered_func'),
    path('edit_func/<str:phone_number>', views.EditFunc.as_view(), name='edit_func'),
    path('remove_func/<str:phone_number>', views.remove_func, name='remove_func')
]