from django.shortcuts import render
from django.http import HttpResponse

doctors= {
    "Иванов Иван Иванович": ["Онколог", '15 лет'],
    "Назарова Ольга Александровна": ["Гематолог", '19 лет'],
    "Самойлов Антон Дмитриевич": ["Врач УЗИ", '12 лет'],
    "Тышкевич Лидия Игнатьевна": ["Онколог", '9 лет']
}

researches=["Биохимический анализ крови", "Общий анализ крови", "Онкотест PanTum Detect", "Инструментальная диагностика", "Цитологические исследования"]

def home_page(request):
    return render(request, "home.html")
def all_researches(request):
    context = {
        "researches": researches,
    }
    return render(request, "researches.html", context=context)

def all_doctors(request):
    context = {
        "doctors": doctors,
    }
    return render(request, "doctors.html", context=context)
def reviews(request):
    return render(request, "reviews.html")
def contacts(request):
    return render(request, "contacts.html")

