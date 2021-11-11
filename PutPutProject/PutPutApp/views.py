from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from PutPutApp.forms import CustomUserCreationForm, AddDrinkForm, OrderForm, RemoveDrinkForm, ManageUserForm, ScorecardForm
from .models import Drink, Orders, Profile, Score, User 
from datetime import date

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
            new_order.location = request.POST['location']
            drink_id = request.POST['drink']
            new_order.drink = get_object_or_404(Drink, pk=drink_id)
            new_order.save()
        return render(request, 'drinks/menu.html')


def orders(request):
    orders = Orders.objects.all()
    return render(
            request, "drinks/orders.html",
            {"orders": orders}
            )

def fulfill_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Orders, pk=order_id)
        order.delete()
        return redirect("orders")



def manage_menu(request):
    if request.method == "GET":
        drink_menu = Drink.objects.all()
        return render(request, 'drinks/manage_menu.html',
                {
                    "add_drink_form": AddDrinkForm,
                    "drink_menu": drink_menu,
                    "remove_drink_form" : RemoveDrinkForm
                    }
                )
    if request.method == "POST" and 'add_drink' in request.POST:
        form = AddDrinkForm(request.POST)
        if form.is_valid():
            new_drink = Drink()
            new_drink.name = request.POST['name']
            new_drink.cost = request.POST['cost']
            new_drink.description = request.POST['description']
            new_drink.save()
        return HttpResponseRedirect(request.path_info)

    if request.method == "POST" and 'remove_drink' in request.POST:
        form = RemoveDrinkForm(request.POST)
        if form.is_valid():
            drink_id = request.POST['drink']
            drink_to_delete = get_object_or_404(Drink, pk=drink_id)
            drink_to_delete.delete()
        return HttpResponseRedirect(request.path_info)

def scorecard(request):
    if request.method == "GET":
        scores = Score.objects.filter(user__exact=request.user).filter(day__exact=date.today())
        return render(request, 'score/scorecard.html', {'scores' : scores, 'form': ScorecardForm})
    if request.method == "POST":
        form = ScorecardForm(request.POST)
        if form.is_valid():

            score = Score(day=date.today(), hole=request.POST['hole'], num_strokes=request.POST['num_strokes'])
            score.save()
            score.user.add(request.user)
    return HttpResponseRedirect(request.path_info)
            

def leaderboard(request):
    return render(request, "PutPutApp/leaderboard.html")

def manage_users(request):
    if request.method == "GET":
        users = Profile.objects.all()
        return render(request, 'manager/manage_users.html',
                {
                    "curUser":request.user,
                    "users": users,
                    "form":ManageUserForm,
                }
        )
    if request.method == "POST":
        form = ManageUserForm(request.POST)
        if form.is_valid():
            user_id = request.POST['user']
            user_type = request.POST['user_type']
            user = get_object_or_404(Profile, pk=user_id)
            user.user_type = user_type[0]
            # print(user, user.user_type)
            user.save()
            print(user.user_type)
        return HttpResponseRedirect(request.path_info)
