from django.urls import path
from . import views

urlpatterns = [
    path("status", views.status, name="status"),
    path("history", views.history, name="history"),
    path("pair", views.pair, name="pair")
]