
from defUserModelprojapp.models import UserDetails
from django import forms

from django.contrib.auth.models import User



class UserForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserDetails
        fields = ['phone','age', 'house_no', 'address','city', 'userpic']