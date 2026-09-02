from django.urls import path


from CBVapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.allCompany.as_view(), name = 'list'),

    path('myclass', views.myClass.as_view()),
    path('home', views.home_view.as_view(), name = 'home'),
    path('<int:pk>/', views.CompanyDetails.as_view(), name='company-detail'),

    path('add', views.AddCompany.as_view(), name = 'add-company'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)