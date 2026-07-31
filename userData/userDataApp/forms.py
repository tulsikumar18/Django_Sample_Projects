
from django import forms

from userDataApp.models import UserData

class UserForms(forms.ModelForm):  # forms.ModelForm is used to save the data to the db..after accepting..
    
    ## create a nested class meta..
    ## model name
    ## no of fields..

    class Meta:
        model = UserData
        fields = '__all__'   # __all__ basically takes all the input here


