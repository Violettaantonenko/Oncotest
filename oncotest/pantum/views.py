from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,login
from .models import Doctors, Research, Reviews, Consultation
from .forms import AddReviewForm, RegisterUserForm, LoginUserForm, UserProfileForm,ConsultationForm
from .utils import *


def home_page(request):
    return render(request, "home.html")


class Researches(DataMixin, ListView):
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

# Личный кабинет
class Profile(DataMixin,CreateView):
    form_class = UserProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

# Запись на консультацию
class AddConsultation(DataMixin, CreateView):
    form_class = ConsultationForm
    template_name = 'consultation.html'
    success_url = reverse_lazy ('home')



#Добавление отзыва
class AddReviews(DataMixin, CreateView):
    form_class = AddReviewForm
    template_name = 'reviews.html'
    success_url = reverse_lazy('reviews')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews']=Reviews.objects.all()
        return context
    # def all_reviews(request):
    #     if request.method == 'POST':
    #         form = AddReviewForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('home')
    #     else:
    #         form = AddReviewForm()
    #     return render(request, "reviews.html", {'form': form})
    #

def contacts(request):
    return render(request, "contacts.html")

# класс регистрации пользователя
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))



# функция для автоматической авторизации пользователя при успешной регистрации
    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('home')

#класс авторизации пользователя
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')