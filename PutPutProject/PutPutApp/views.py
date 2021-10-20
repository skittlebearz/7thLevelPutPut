from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from PutPutApp.forms import CustomUserCreationForm, ReservationForm
from .models import Calandar
# Create your views here.
def dashboard(request):
    return render(request, "PutPutApp/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "PutPutApp/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = Calandar()
            reservation.day = request.POST['date'] 
            reservation.save()

        return render(request, 'reservation.html')
    else:
        return render(request, 'reservation.html')
