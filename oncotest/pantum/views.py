from django.shortcuts import render
from django.http import HttpResponse

doctors=["Иванов Иван Иванович", "Назарова Ольга Александровна","Самойлов Антон Дмитриевич","Тышкевич Лидия Игнатьевна"]
def all_doctors(request):
    return render (request, "pantum.html",{"doctors":doctors})
