from django.shortcuts import render

from userDataApp.forms import UserForms

# Create your views here.

def index(request):

    form = UserForms()
    return render(request, 'index.html', {'form': form})
