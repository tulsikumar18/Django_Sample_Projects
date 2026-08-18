
from defUserModelprojapp.models import UserDetails,VendorDetails
from django import forms

from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput) # this is used to display the password in the **** form..

    class Meta:

        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserDetails
        fields = [
            'phone',
            'age',
            'house_no',
            'street',
            'address',
            'city',
            'state',
            'zipcode',
            'userpic'
        ]
    captcha = ReCaptchaField()



class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


# created to update the 2nd forms data..
class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = UserDetails
        fields = ['phone','age', 'house_no', 'address','city', 'userpic']


## vendorDetails Form..

class VendorDetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = VendorDetails
        fields = [
            'vendor_name',
            'vendor_email',
            'password',
            'restaurant_name',
            'phone_no',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'gst_no',
            'license_img',
            'restaurant_img',
        ]
    captcha = ReCaptchaField()