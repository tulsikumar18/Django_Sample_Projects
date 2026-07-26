
from django.shortcuts import render

from internaldbapp.models import STUDENT

# Create your views here.

def index(request):

    std_details = STUDENT.objects.all()        # it is used to fetch all the objects from the model...in the form of dictionary

    return render(request,'index.html',{'std_details' : std_details})