from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from .models import Drink, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")

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
    location = forms.IntegerField(label="Hole Number", validators=[MinValueValidator(1),MaxValueValidator(18)])

class RemoveDrinkForm(forms.Form):
    menu = Drink.objects.all()
    drink = forms.ModelChoiceField(
            queryset=menu,
            required=True,
            widget=forms.RadioSelect)


class DateInput(forms.DateInput):
    input_type = 'date'

class SponsorForm(forms.Form):
    date = forms.DateField(widget=DateInput, label="Enter date to reserve for tournament")
    tournament_name = forms.CharField(max_length=60)

class ScorecardForm(forms.Form):
    hole = forms.IntegerField(label="Hole Number", validators=[MinValueValidator(1),MaxValueValidator(18)])
    num_strokes = forms.IntegerField(label="Number of Strokes", validators=[MinValueValidator(1),MaxValueValidator(99)])


class ManageUserForm(forms.Form):
    menu = Profile.objects.all()
    user = forms.ModelChoiceField(
            queryset=menu,
            required=True,
            widget=forms.RadioSelect
    )
    CHOICES=[("Player","Player"), ("Manager","Manager"), ("Sponsor","Sponsor")]

    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple, required=True)

class DepositFundsForm(forms.Form):
    amount = forms.DecimalField(label="Deposit Amount", max_digits=9, decimal_places=2)
