from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
# Create your views here.

def review(request):
    if request.method == 'POST':
        existing_data = Review.objects.get(pk=1)
        form = ReviewForm(request.POST, instance=existing_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm() # New Empty Form

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
