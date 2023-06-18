from django.urls import path
from .views import all_doctors


urlpatterns = [
    path('home/', all_doctors)

]