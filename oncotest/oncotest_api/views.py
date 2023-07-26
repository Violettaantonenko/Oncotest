from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pantum.models import Clients, Doctors, Consultation, Research, Reviews
from .serializers import ClientsSerializer, DoctorsSerializer, ConsultationSerializer, ResearchSerializer, \
    ReviewsSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics


# Create your views here.


# возможность читать, изменять, удалять запись
class ClientsListAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

    # def get(self, request, format=None):
    #     clients = Clients.objects.all()
    #     serializer_data = ClientsSerializer(clients, many=True).data
    #     return Response(serializer_data)
    #
    # def post(self, request, format=None):
    #     serializer = ClientsSerializer(data=request.data)  #принимаем данные с нашего запроса
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorsListAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer


class ConsultationListAPIView(generics.ListCreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class ConsultationListAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class ResearchAPIView(APIView):
    def get(self, request, format=None):
        place = Research.objects.all()
        serializer_data = ResearchSerializer(place,
                                             many=True).data  # many=true - набор запросов содержит несколько элементов (списков элементов)
        return Response(serializer_data)


class ReviewsAPIView(APIView):
    def get(self, request, format=None):
        place = Reviews.objects.all()
        serializer_data = ReviewsSerializer(place, many=True).data
        return Response(serializer_data)
