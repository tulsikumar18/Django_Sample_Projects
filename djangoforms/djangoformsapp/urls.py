# when we have more than 2 html pages.. we use the app urls.py

from django.urls import path

from djangoformsapp import views

urlpatterns = [

    path('', views.index),
    path('display',views.display),
    path('about', views.about),
    path('contact', views.contact),
]