from django.conf.urls import include
from django.urls import path
from PutPutApp.views import dashboard, register, menu, manage_menu, orders, login, fulfill_order, leaderboard, manage_users


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("menu/", menu, name="menu"),
    path("managemenu/", manage_menu, name="manage_menu"),
    path("manageusers/", manage_users, name="manage_users"),
    path("orders/", orders, name="orders"),
    path("leaderboard/", leaderboard, name="leaderboard"),
    path("orders/<int:order_id>", fulfill_order, name='fulfill_order'),

]
