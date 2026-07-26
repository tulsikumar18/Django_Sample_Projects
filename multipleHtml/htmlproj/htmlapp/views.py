from django.shortcuts import render



def first_view(request):

    details = {

        'name' : 'Pyspiders',
        'names' : ['shalini', 'mounika','shraddha','Kriti'],
        'std_details' : (
            {'name' : 'one', 'age' : 16,'degree': 'BE','streams': 'CS','address': 'bangalore', 'marks': 75, 'grade': 'A', 'skills' : ['C', 'java', 'C++', 'python']},
            {'name' : 'Two', 'age' : 20,'degree': 'BE','streams': 'AIML','address': 'mangalore', 'marks': 65, 'grade': 'b', 'skills' : ['C', 'java', 'C++', 'python']}
        )

    }
    
   

    return render (request, 'one.html' , context = details)


def second_view(request):

    return render(request, 'two.html') 

def third_view(request):

    return render(request,'three.html')

def four_view(request):

    return render(request,'four.html')


def result(request):

    # n1 = int(request.GET['num1'])                   ## typecasting has to be done to get numerical value , otherwise it is string value.. 
    # n2 = int(request.GET['num2'])                   ## GET method is used to get the value of the data.. 

    n1 = int(request.POST['num1'])                   ## POST method is used to add data , whenever there is a form ,we always use Post method
    n2 = int(request.POST['num2'])


    ## Approach 1 : request will have the name of the button in the POST data , so we check the name of the button to perform the operation..

    # if 'add' in request.POST:
    #     res = n1 + n2
    # elif 'sub' in request.POST:
    #     res = abs(n1-n2)
    # elif 'mul' in request.POST:
    #     res = n1 * n2
    # elif 'div' in request.POST:
    #     if n2 == 0:
    #         res = 'zero Division Error'
    #     else:
    #         res = n1 / n2
    # elif 'mod' in request.POST:
    #     res = n1 % n2

    #  Another approach is to get the operation by name and match it using match case..

    opr = request.POST['operation']

    match opr:
        case 'add':

            res =  n1 + n2
        case 'sub':
            res =  abs(n1-n2)
        case 'mul':
            res = n1 * n2
        
        case 'div': 
            if n2 == 0:
                res = 'Zero Division Error'
            else:
                res = n1/n2

        case 'mod':
            res = n1 % n2


    return render(request, 'result.html', context= {'res': res})

