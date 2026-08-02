from djangoformsapp.models import UserInfo
from django.shortcuts import render

from djangoformsapp.forms import UserForms

# Create your views here.


def index(request):

    form = UserForms()

    if request.method == 'POST':

        form = UserForms(request.POST,request.FILES) ## here request.post handles the normal data, to handle the media data we use the request.files

        if form.is_valid():
            print('validation Success')
            form.save()

    return render(request,'index.html', {'form': form})

def display(request):

    data = UserInfo.objects.all()

    return render(request, 'display.html', {'data': data})


def about(request):

    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
    


