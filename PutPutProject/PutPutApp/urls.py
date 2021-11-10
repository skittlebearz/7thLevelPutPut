from django.conf.urls import include
from django.urls import path
from PutPutApp.views import *

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("menu/", menu, name="menu"),
    path("managemenu/", manage_menu, name="manage_menu"),
    path("orders/", orders, name="orders"),
    path("orders/<int:order_id>", fulfill_order, name='fulfill_order'),
    path("", dashboard, name="dashboard"),
    path("scorecard/", scorecard, name="scorecard")
]
