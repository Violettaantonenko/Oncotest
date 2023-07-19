from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_page, name='home'),
    path('doctors/', all_doctors, name='doctors'),
    path('research/', Researches.as_view(), name='research'),
    path('reviews/', AddReviews.as_view(), name='reviews'),
    path('contacts/', contacts, name='contacts'),
    # path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),


]