from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [

    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('contact/', views.contact, name="contact"),

]
