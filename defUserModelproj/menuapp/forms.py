
from menuapp.models import FoodItems
from django import forms


class MenuForms(forms.ModelForm):

    class Meta:

        model = FoodItems
        fields = [
            'name',
            'price',
            'img',
            'category',
        ]
