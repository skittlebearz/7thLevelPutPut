from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from .models import Drink

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class AddDrinkForm(forms.Form):
    name = forms.CharField(label="Drink name")
    cost = forms.DecimalField(label="Drink Cost")
    description = forms.CharField(label="Drink Description")


class OrderForm(forms.Form):
    menu = Drink.objects.all()
    name = forms.CharField(max_length=30)
    drink = forms.ModelChoiceField(
            queryset=menu,
            required=True,
            widget=forms.RadioSelect)
    location = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(18)])

class RemoveDrinkForm(forms.Form):
    menu = Drink.objects.all()
    drink = forms.ModelChoiceField(
            queryset=menu,
            required=True,
            widget=forms.RadioSelect)



