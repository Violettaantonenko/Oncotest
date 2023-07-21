from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_page, name='home'),
    path('doctors/', all_doctors, name='doctors'),
    path('research/', Researches.as_view(), name='research'),
    path('reviews/', AddReviews.as_view(), name='reviews'),
    path('contacts/', contacts, name='contacts'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', Profile.as_view(), name='profile')



]