from django.shortcuts import render

from formsapp.forms import UserForms

# Create your views here.


def index(request):

    forms = UserForms()


    return render(request,'index.html',{'forms': forms})
