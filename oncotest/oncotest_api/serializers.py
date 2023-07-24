from rest_framework import serializers
from pantum.models import Clients, Doctors, Consultation, Research,Reviews

#отобразить в Readmi описание REST API
#Вывод данных клиента
class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ("surname","name","fathername","age","phone","email","city")

    def create(self, validated_data):
        return Clients.objects.create(**validated_data)


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ("surname","name","fathername","age","specialization","experience")

    def create(self, validated_data):
        return Doctors.objects.create(**validated_data)

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ("clients", "service","date","phone")

    def create(self, validated_data):
        return Consultation.objects.create(**validated_data)

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ("name","description")

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ("clients","rating","description")