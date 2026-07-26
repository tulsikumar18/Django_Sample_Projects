from django.shortcuts import render

# Create your views here.

def index(request):

    context = {

        'message' : 'I am not in Danger , I am the Danger , Remember My name..'
    }

    return render(request, 'index.html', context)


def result(request):

    return render(request, 'result.html')