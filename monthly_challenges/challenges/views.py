from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes a day!"
    elif month == "march":
        challenge_text = "Learn Django"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(f"{month} challenge: {challenge_text}")

def monthly_challenge_by_number(request, month):
    return HttpResponse(f"Entered month number is: {month}")