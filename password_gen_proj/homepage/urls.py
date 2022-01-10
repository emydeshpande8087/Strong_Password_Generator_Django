from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('gen_password', views.gen_password, name='password'),
]