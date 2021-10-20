from django.conf.urls import include
from django.urls import path
from PutPutApp.views import dashboard, register, reservation

urlpatterns = [
    path("register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("reservation/", reservation, name="reservation"),
]
