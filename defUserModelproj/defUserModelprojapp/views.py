
from defUserModelprojapp.models import VendorDetails

from menuapp.forms import MenuForms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from defUserModelprojapp.forms import UserForm, UserProfileForm , UserUpdateForm , UserProfileUpdateForm
from defUserModelprojapp.forms import VendorDetailsForm


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

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            if user.is_active:

                login(request, user)

                # Check whether this user is a vendor
                if hasattr(user, 'vendor'):

                    if user.vendor.is_approved:
                        return redirect('dashboard')
                    
                    else:
                        logout(request)
                        return HttpResponse('Your Account is Waiting for Admin Approval...')

                # Otherwise normal user
                return redirect('home')

            else:
                return HttpResponse('User is Inactive..')

        else:
            return HttpResponse(
                'Please check your credentials..'
            )

    return render(request, 'login.html', {})




@login_required(login_url='login')
def home(request):
    
    vendors = VendorDetails.objects.filter(is_approved = True)    ## it is used to access the details of all  the approved Vendor...

    return render(request, 'home.html', {'vendors': vendors})  # it returns the data in the form of QuerySet..


@login_required(login_url='login')
def user_profile(request):
    
    return render(request, 'profile.html',{})

@login_required(login_url= 'login')
def user_logout(request):

    logout(request)

    return redirect('login')

@login_required(login_url = 'login')
def update(request):

    form1 = UserUpdateForm(instance=request.user)
    form2 = UserProfileUpdateForm(instance=request.user.userdetails)

    if request.method == 'POST':

        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = UserProfileUpdateForm( request.POST, request.FILES,instance=request.user.userdetails)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')
    return render(request, 'update.html',{'form1': form1 , 'form2' : form2})





def vendor_reg(request):

    if request.method == 'POST':

        form1 = VendorDetailsForm(request.POST,request.FILES)

        if form1.is_valid():

            # Get form data
            vendor_name = form1.cleaned_data['vendor_name']
            vendor_email = form1.cleaned_data['vendor_email']
            password = form1.cleaned_data['password']

            # Create Django User
            user = User.objects.create_user(
                username=vendor_name,
                email=vendor_email,
                password=password
            )

            # Create VendorDetails
            vendor = form1.save(commit=False)
            vendor.user = user
            vendor.save()

            # Go to common login page
            return redirect('login')

    else:

        form1 = VendorDetailsForm()

    return render(request,'vendor_reg.html',{'form1': form1})



## dashboard.. will return me the four Queryset..
@login_required(login_url='login')
def dashboard(request):

    vendor = request.user.vendor   ## it is used to access the details of the logged in Vendor...
    
    return render(request, 'dashboard.html' , {'vendor': vendor})




## food menu...

@login_required(login_url = 'login')
def foodmenu(request):

    form1 = MenuForms()

    return render(request, 'foodmenu.html', {'form1': form1})