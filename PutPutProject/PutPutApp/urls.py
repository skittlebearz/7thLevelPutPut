from django.conf.urls import include
from django.urls import path
from PutPutApp.views import dashboard, register, menu, manage_menu, orders

urlpatterns = [
    path("register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("menu/", menu, name="menu"),
    path("managemenu/", manage_menu, name="manage_menu"),
    path("orders/", orders, name="orders"),
]
