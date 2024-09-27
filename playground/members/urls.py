from . import views
from django.urls import path

app_name = 'members'

urlpatterns = [
    path('', views.registerForm, name="register"),
    path('success/', views.success, name='success')
]
