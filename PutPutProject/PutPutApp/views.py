from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.db.models import Sum

from PutPutApp.forms import *
from .models import Drink, Orders, Profile, Score, Calendar, SponsorRequest, User

@login_required
def dashboard(request):
    return render(request, "PutPutApp/dashboard.html")

def Login(request):
    return render(request, "registration/login.html")

def register(request):
    if request.method == "GET":
        events = Calendar.objects.all()
        return render(
            request, "PutPutApp/register.html",
            {"form": CustomUserCreationForm,
             "events": events}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

@login_required
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

@login_required
def orders(request):
    orders = Orders.objects.all()
    return render(
            request, "drinks/orders.html",
            {"orders": orders}
            )

@login_required
def fulfill_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Orders, pk=order_id)
        order.delete()
        return redirect("orders")

@login_required
def sponsor_requests(request):
    if request.method == "GET":
        events = Calendar.objects.all()
        reservation_requests = SponsorRequest.objects.all()
        return render(request, 'tournament/sponsor_requests.html', 
                {"requests": reservation_requests,
                "events": events}
                )

@login_required
def approve_tournament(request, sponsor_request_id):
    if request.method == "POST":
        reservation = get_object_or_404(SponsorRequest, pk=sponsor_request_id)
        if "Approve" in request.POST:
            tournament = Calendar()
            tournament.day = reservation.day
            tournament.tournament_name = reservation.tournament_name
            #tournament.sponsor = reservation.sponsor
            tournament.save()
        reservation.delete()
        return redirect("sponsor_requests")

@login_required
def sponsor(request):
    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            reservation_request = SponsorRequest()
            reservation_request.day = request.POST['date']
            reservation_request.tournament_name = request.POST['tournament_name']
            reservation_request.save()

        return HttpResponseRedirect(request.path_info)
    elif request.method == "GET":
        events = Calendar.objects.all()
        return render(request, 'tournament/sponsor.html', 
                {"form": SponsorForm,
                "events": events}
                )


@login_required
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

@login_required
def scorecard(request):
    if request.method == "GET":
        scores = Score.objects.filter(user__exact=request.user).filter(day__exact=date.today()).order_by('hole').values('hole', 'num_strokes', 'par')
        total_score = Score.objects.filter(user__exact=request.user).filter(day__exact=date.today()).aggregate(Sum('num_strokes'))['num_strokes__sum']
        total_par = Score.objects.filter(user__exact=request.user).filter(day__exact=date.today()).aggregate(Sum('par'))['par__sum']
        holes = []
        for i in range(18):
            holes.append({'hole' : i+1, 'num_strokes' : 0})
        for i in scores:
            holes[i['hole'] - 1] = i
        return render(request, 'score/scorecard.html', {'scores' : holes, 'form': ScorecardForm, 'form' : ScorecardForm, 'total_score' : total_score, 'total_par' : total_par})
    if request.method == "POST":
        form = ScorecardForm(request.POST)
        if form.is_valid():
            score = Score(day=date.today(), hole=request.POST['hole'], num_strokes=request.POST['num_strokes'])
            score.save()
            score.user.add(request.user)
    return HttpResponseRedirect(request.path_info)
            

@login_required
def leaderboard(request):
    if request.method == "GET":
        scores = Score.objects.filter(user__exact=request.user).filter(day__exact=date.today()).order_by('hole').values('hole', 'num_strokes')
        holes = []
        print(scores)
        for i in range(18):
            holes.append({'hole' : i+1, 'num_strokes' : 0})
        for i in scores:
            print(i)
            holes[i['hole'] - 1] = i
        total_score = 0
        total_par = 0
        for i in holes:
            i['par'] = i['num_strokes'] - 3 if i['num_strokes'] != 0 else 0
            total_score += i['num_strokes']
            total_par += i['par']
        return render(request, 'score/leaderboard.html', {'scores' : holes, 'form': ScorecardForm, 'form' : ScorecardForm, 'total_score' : total_score, 'total_par' : total_par})

@login_required
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
