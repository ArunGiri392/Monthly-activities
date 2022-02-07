from django.urls import path
from . import views
urlpatterns =[ 
    path("", views.home, name="index"),
    path("<int:month>", views.monthly_challenge_bynumbers),
    path('<str:month>', views.monthly_challenge, name="month_challenge")
]