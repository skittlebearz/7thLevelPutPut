from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class ReservationForm(forms.Form):
    date = forms.DateField(label="Enter date to reserve for tournament")
