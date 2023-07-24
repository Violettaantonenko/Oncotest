from django.urls import path
from .views import *

urlpatterns = [
    path('clients/<int:pk>/', ClientsListAPIViewDetail.as_view()),
    path('doctors/<int:pk>/', DoctorsListAPIViewDetail.as_view()),
    path('consultation/',ConsultationListAPIView.as_view()),
    path('consultation/<int:pk>/', ConsultationListAPIViewDetail.as_view()),
    path('research/',ResearchAPIView.as_view()),
    path('reviews/',ReviewsAPIView.as_view()),
]