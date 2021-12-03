from django.conf.urls import include
from django.urls import path
from PutPutApp.views import dashboard, register, menu, manage_menu, orders, login, fulfill_order, leaderboard, manage_users, sponsor, sponsor_requests, approve_tournament
from PutPutApp.views import *


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("menu/", menu, name="menu"),
    path("managemenu/", manage_menu, name="manage_menu"),
    path("manageusers/", manage_users, name="manage_users"),
    path("orders/", orders, name="orders"),
    path("leaderboard/", leaderboard, name="leaderboard"),
    path("orders/<int:order_id>", fulfill_order, name='fulfill_order'),
    path("", dashboard, name="dashboard"),
    path("scorecard/", scorecard, name="scorecard"),
    path("sponsor/", sponsor, name="sponsor"),
    path("managetournaments/", sponsor_requests, name="sponsor_requests"),
    path("managetournaments/<int:sponsor_request_id>", approve_tournament, name="approve_tournament"),
    path("deposit/", deposit_funds, name="deposit_funds"),
]
