from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse


monthly_challenges = {
    "january":"Eat no meat for the month",
    "february": "Go to the gym",
    "March": "Learn django",
    "April": 'Go to the gym',
    "May": 'Learn django',
    "June": "Eat no meat for the month",
    "July": "Learn django ",
    "August": "Go to the gym",
    "September": "Eat no meat for the month",
    "October": "Learn django ",
    "November": "Go to the gym ",
    "December": None
}
# Create your views here.
def home(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"all_months":months})
    

    

def monthly_challenge_bynumbers(request, month):
    if month <= 12:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month_challenge",args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("Invalid input")
  

def monthly_challenge(request, month):
    
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text":challenge_text, "month_name":month})
    except:
        raise Http404()

    