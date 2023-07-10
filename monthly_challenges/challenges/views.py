from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

# Create your views here.
def index(request):
    htmlLIs = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_url = reverse("monthly-challenge", args=[month])
        htmlLIs += f"<li><a href=\"{month_url}\">{month.capitalize()}</a></li>"

    return HttpResponse(f"<ul>{htmlLIs}</ul>")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponse("<h1>This month is not supported!</h1>")

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        if month > len(months):
            return HttpResponseNotFound("Invalid Month")
        month = months[month - 1]
        redirect_month_url = reverse("monthly-challenge", args=[month]) # ex: /challenge/january
        return HttpResponseRedirect(f"<h1>{redirect_month_url}<h1/>")
    except:
        return HttpResponseNotFound("<h1/>This month is not supported!<h1/>")
