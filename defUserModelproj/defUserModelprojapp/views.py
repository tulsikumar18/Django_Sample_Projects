
from sqlalchemy.util.langhelpers import repr_tuple_names
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout 
from django.shortcuts import render,redirect
from defUserModelprojapp.forms import UserForm, UserProfileForm , UserUpdateForm , UserProfileUpdateForm

# Create your views here.


def register(request):
    registered = False

    if request.method == "POST":
        
        form1 = UserForm(request.POST)
        form2 = UserProfileForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            
            user = form1.save()
            user.set_password(user.password) # this will encrypt the password using hashing technique before saving it..
            user.save()

            profile = form2.save( commit= False)
            
            # merge the two fields.
            profile.user = user

            # save it now..
            profile.save()
            registered = True # once registred , make it true.., so that Thank you message appears..

    else:

        form1 = UserForm()
        form2 = UserProfileForm()
    return render(request,'registration.html',{'form1' : form1 , 'form2' : form2 , 'registered' : registered})      





def user_login(request):

    if request.method == 'POST': 

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password) # authenticate method is used to authenticate the register and login page

        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')

            else:
                return HttpResponse('User is Inactive..')
        else:
            return HttpResponse('Please check your credentials..')
    


    return render(request, 'login.html',{})


@login_required(login_url='login')
def home(request):

    return render(request,'home.html')


@login_required(login_url='login')
def user_profile(request):
    
    return render(request, 'profile.html',{})

@login_required(login_url= 'login')
def user_logout(request):

    logout(request)

    return redirect('login')

@login_required(login_url = 'login')
def update(request):

    form1 = UserUpdateForm(request.POST, instance=request.user)
    form2 = UserProfileUpdateForm(instance=request.user.userdetials)

    if request.method == 'POST':

        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = UserProfileUpdateForm(instance=request.user.userdetials)

        if form1.is_valid():
            form1.save()
            return redirect('profile')
    return render(request, 'update.html',{'form1': form1 , 'form2' : form2})