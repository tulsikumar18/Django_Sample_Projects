
from django.urls import path
from htmlapp import views


urlpatterns = [

    path('',views.first_view),
    path('two',views.second_view),
    path('third',views.third_view),
    path('four',views.four_view),
    path('result', views.result)

]