
## import forms from django


from django import forms

class UserForms(forms.Form):


    name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    email = forms.EmailField()
    marks = forms.IntegerField()
