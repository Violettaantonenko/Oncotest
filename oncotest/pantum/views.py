from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Doctors, Research


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
def reviews(request):
    return render(request, "reviews.html")
def contacts(request):
    return render(request, "contacts.html")

