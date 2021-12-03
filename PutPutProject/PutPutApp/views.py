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
    if not request.user.profile.player:
        return HttpResponseRedirect('/dashboard')
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
    if not request.user.profile.barkeep:
        return HttpResponseRedirect('/dashboard')
    orders = Orders.objects.all()
    return render(
            request, "drinks/orders.html",
            {"orders": orders}
            )

@login_required
def fulfill_order(request, order_id):
    if not request.user.profile.barkeep:
        return HttpResponseRedirect('/dashboard')
    if request.method == "POST":
        order = get_object_or_404(Orders, pk=order_id)
        order.delete()
        return redirect("orders")

@login_required
def sponsor_requests(request):
    if not request.user.profile.manager:
        return HttpResponseRedirect('/dashboard')
    if request.method == "GET":
        events = Calendar.objects.all()
        reservation_requests = SponsorRequest.objects.all()
        return render(request, 'tournament/sponsor_requests.html', 
                {"requests": reservation_requests,
                "events": events}
                )

@login_required
def approve_tournament(request, sponsor_request_id):
    if not request.user.profile.manager:
        return HttpResponseRedirect('/dashboard')
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
    if not request.user.profile.sponsor:
        return HttpResponseRedirect('/dashboard')
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
    if not request.user.profile.manager:
        return HttpResponseRedirect('/dashboard')
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
    if not request.user.profile.player:
        return HttpResponseRedirect('/dashboard')
    if request.method == "GET":
        scores = Score.objects.filter(user__exact=request.user).filter(day__exact=date.today()).order_by('hole').values('hole', 'num_strokes', 'par')
        total_score = Score.objects.filter(user__exact=request.user).filter(day__exact=date.today()).aggregate(Sum('num_strokes'))['num_strokes__sum']
        total_par = Score.objects.filter(user__exact=request.user).filter(day__exact=date.today()).aggregate(Sum('par'))['par__sum']
        holes = []
        for i in range(18):
            holes.append({'hole' : i+1, 'num_strokes' : 0})
        for i in scores:
            holes[i['hole'] - 1] = i
        return render(request, 'score/scorecard.html', {'scores' : holes, 'form' : ScorecardForm, 'total_score' : total_score, 'total_par' : total_par})
    if request.method == "POST":
        form = ScorecardForm(request.POST)
        if form.is_valid():
            score = Score(day=date.today(), hole=request.POST['hole'], num_strokes=request.POST['num_strokes'])
            score.save()
            score.user.add(request.user)
            score.save()
    return HttpResponseRedirect(request.path_info)
            

@login_required
def leaderboard(request):
    if not user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == "GET":
        scores = Score.objects.filter(day__exact=date.today()).values('user').annotate(total_score=Sum('num_strokes'), total_par=Sum('par')).order_by('total_score').values('total_score', 'total_par', 'user__first_name', 'user__last_name')
        for i in range(len(scores)):
            scores[i]['count'] = i + 1
        return render(request, 'score/leaderboard.html', {'leaderboard' : scores})

@login_required
def manage_users(request):
    if not request.user.profile.manager:
        return HttpResponseRedirect('/dashboard')
    if request.method == "GET":
        users = Profile.objects.all().values('id', 'user__first_name', 'user__last_name', 'player', 'barkeep', 'sponsor', 'manager')
        print(users)
        return render(request, 'manager/manage_users.html', {"users": users})
    if request.method == "POST":
        new_permissions = dict(request.POST) 
        new_permissions.pop('csrfmiddlewaretoken')
        for key, value in new_permissions.items():
            user = Profile.objects.get(id=key)
            user.manager = 'manager' in value
            user.sponsor = 'sponsor' in value
            user.barkeep = 'barkeep' in value
            user.player  = 'player' in value
            user.save()
        return HttpResponseRedirect(request.path_info)
        
    
#    if request.method == "GET":
#        users = Profile.objects.all()
#        return render(request, 'manager/manage_users.html',
#                {
#                    "curUser":request.user,
#                    "users": users,
#                    "form":ManageUserForm,
#                }
#        )
#    if request.method == "POST":
#        form = ManageUserForm(request.POST)
#        if form.is_valid():
#            user_id = request.POST['user']
#            user_type = request.POST['user_type']
#            user = get_object_or_404(Profile, pk=user_id)
#            user.user_type = user_type[0]
#            # print(user, user.user_type)
#            user.save()
#            print(user.user_type)
#        return HttpResponseRedirect(request.path_info)

def deposit_funds(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == "GET":
        return render(request, 'PutPutApp/deposit.html', {'form' : DepositFundsForm})
    if request.method == "POST":
        form = DepositFundsForm(request.POST)
        if form.is_valid():
            prof = Profile.objects.get(user=request.user)
            prof.account_balance = float(prof.account_balance) + float(request.POST['amount'])
            prof.save()
    return HttpResponseRedirect(request.path_info)


