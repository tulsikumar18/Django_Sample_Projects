
from django.shortcuts import render
from defUserModelprojapp.forms import UserForm,UserProfileForm

# Create your views here.


def register(request):
    form1 = UserForm()
    form2 = UserProfileForm()

    return render(request,'registration.html',{'form1' : form1 , 'form2' : form2})