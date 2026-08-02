
from django import forms

from djangoformsapp.models import UserInfo

class UserForms(forms.ModelForm):

    class Meta: 
        
        model = UserInfo
        fields = '__all__'