from django.urls import path

from myapp import views


urlpatterns = [


    path('', views.index_view),

    path('result', views.result_view)
]