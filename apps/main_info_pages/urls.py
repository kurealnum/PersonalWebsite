from django.urls import path
from . import views

urlpatterns = [
    #base template 
    path('', views.layout, name='layout'),

    path('home/', views.home, name="home"),
    path('aboutme/', views.aboutme, name='aboutme'),
]