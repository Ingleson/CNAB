from django.urls import path
from . import views

urlpatterns = [
    path("transaction/", views.TransactionView.as_view()),
]