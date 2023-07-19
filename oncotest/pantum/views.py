from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Doctors, Research
from .forms import AddReviewForm, RegisterUserForm
from .utils import *



def home_page(request):
    return render(request, "home.html")


class Researches(DataMixin,ListView):
    model = Research
    template_name = 'researches.html'
    context_object_name = "research"



# def all_researches(request):
#     context = {
#         "research": Research.objects.all(),
#     }
#     return render(request, "researches.html", context=context)


def all_doctors(request):
    context = {
        "doctors": Doctors.objects.all(),
    }
    return render(request, "doctors.html", context=context)

class AddReviews(DataMixin, CreateView):
    form_class = AddReviewForm
    template_name = 'reviews.html'
    success_url = reverse_lazy('home')

# def all_reviews(request):
#     if request.method == 'POST':
#         form = AddReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddReviewForm()
#     return render(request, "reviews.html", {'form': form})


def contacts(request):
    return render(request, "contacts.html")
# перепроверить и создать класс Миксинов в утилс
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy ('login')

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

