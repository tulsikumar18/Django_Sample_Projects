
# To link multiple html pages , we create views in myapp1
# But if a single html page then it can be called in views in the myproj1 

# we need the views of myapp1 and path information to create views.
#After include the views in myapp1, we need to inform the views of myproj1 that i am calling all 
#the views in myapp1 only..



from django.urls import path
from myapp1 import views

urlpatterns = [

    path('', views.firstview)
]



