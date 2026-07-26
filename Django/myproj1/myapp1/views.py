from django.shortcuts import render

# Create your views here.

# to link a multiple html pages, create a multiple views..

# def firstpage(request):

#     return render(request, 'first.html')

# def secondpage(request):
#     return render(request, 'second.html')

# def thirdpage(request):
#     return render(request, 'third.html')



def firstview(request):

    context = {

        'name': 'Tulsi Kumar',
        'age' : 23,
        'place' : ['Banglore','Mysuru','Belgavi','Sri Lanka'],
        'l' : [12,13,87,35,98]
    }
    return render(request, 'first.html', context)