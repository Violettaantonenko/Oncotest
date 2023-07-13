from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Doctors, Research, Reviews
from .forms import AddReviewForm


def home_page(request):
    return render(request, "home.html")


def all_researches(request):
    context = {
        "research": Research.objects.all(),
    }
    return render(request, "researches.html", context=context)


def all_doctors(request):
    context = {
        "doctors": Doctors.objects.all(),
    }
    return render(request, "doctors.html", context=context)


def all_reviews(request):
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            print(form)
    else:
        form = AddReviewForm()

    # context = {
    #     "form": form
    #     "reviews": Reviews.objects.all()
    # }
    return render(request, "reviews.html", {'form': form})


def contacts(request):
    return render(request, "contacts.html")

