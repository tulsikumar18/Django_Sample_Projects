
from menuapp.models import FoodItems
from django import forms


class MenuForms(forms.ModelForm):

    class Meta:

        model = FoodItems
        fields = '__all__'
