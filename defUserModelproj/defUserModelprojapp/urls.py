from django.urls import path
from defUserModelprojapp import views

urlpatterns = [
    path('', views.register , name = 'register'),
    path('login',views.user_login, name = 'login'),
    path('home', views.home, name = 'home'),
    path('logout', views.user_logout, name = 'logout'),
    path('profile', views.user_profile , name = 'profile'),
    path('update', views.update,name = 'update')
]
