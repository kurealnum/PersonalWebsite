from django.urls import path
from . import views

urlpatterns = [
    #base template 
    path('', views.layout, name='layout'),

    path('home/', views.index, name="index"),
]