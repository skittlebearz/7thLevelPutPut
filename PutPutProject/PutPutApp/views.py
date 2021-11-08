from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from PutPutApp.forms import CustomUserCreationForm, AddDrinkForm, OrderForm
from .models import Drink, Orders
# Create your views here.
def dashboard(request):
    return render(request, "PutPutApp/dashboard.html")

def Login(request):
    return render(request, "registration/login.html")

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

def menu(request):
    if request.method == "GET":
        drink_menu = Drink.objects.all()
        return render(
                request, "drinks/menu.html",
                {"drink_menu": drink_menu,
                    "form": OrderForm
                    }
                )
    elif request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = Orders()
            new_order.name = request.POST['name']
            new_order.drink = request.POST['drink']
            new_order.location = request.POST['location']
            new_order.save()
        return render(request, 'drinks/menu.html')


def orders(request):
    orders = Orders.objects.all()
    return render(
            request, "drinks/orders.html",
            {"orders": orders}
            )

def manage_menu(request):
    if request.method == "GET":
        drink_menu = Drink.objects.all()
        return render(request, 'drinks/manage_menu.html',
                {
                    "form": AddDrinkForm,
                    "drink_menu": drink_menu
                    }
                )
    if request.method == "POST":
        form = AddDrinkForm(request.POST)
        if form.is_valid():
            new_drink = Drink()
            new_drink.name = request.POST['name']
            new_drink.cost = request.POST['cost']
            new_drink.description = request.POST['description']
            new_drink.save()
        return render(request, 'drinks/manage_menu.html')

def leaderboard(request):
    return render(request, "PutPutApp/leaderboard.html")
