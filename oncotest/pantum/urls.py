from django.urls import path
from .views import home_page, all_doctors,all_researches,reviews,contacts


urlpatterns = [
    path('home/', home_page, name='home'),
    path('doctors/', all_doctors, name='doctors'),
    path('research/', all_researches, name='research'),
    path('reviews/', reviews, name='reviews'),
    path('contacts/', contacts, name='contacts'),

]