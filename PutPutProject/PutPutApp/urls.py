from django.conf.urls import include
from django.urls import path
from PutPutApp.views import dashboard, register

urlpatterns = [
    path("register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
]
