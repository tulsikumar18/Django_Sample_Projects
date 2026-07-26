from django.shortcuts import render

# Create your views here.

def index_view(request):

    return render(request, 'index.html')


def result_view(request):

    n1 = int(request.POST['num1'])   # If data is sent to the url , then in the GET method  data is visible in the url
    n2 = int(request.POST['num2'])  # However in the POST method , the data is not visible in the url it is hidden.

    op = request.POST['operation']

    if op == 'ADD':
        res = n1 + n2
    elif op == 'SUB':
        res = n1 - n2
    elif op == 'MUL':
        res = n1 * n2
    elif op == 'DIV':
        res = n1 / n2
    elif op == 'MOD':
        res = n1 % n2
    else:
        res = n1 ** n2

    return render(request, 'result.html', {'res' : res})

