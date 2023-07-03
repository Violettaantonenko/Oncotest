from django.db import models

SPECIALIZATION = [
    ('Гематолог', 'Врач-гематолог'),
    ('Онколог', 'Врач-онколог'),
    ('Терапев', 'Врач-терапевт'),
    ('Врач УЗД', 'Врач ультразвуковой диагностики'),
    ('Врач КДЛ', 'Врач клинико-лабораторной диагностики'),

]

RESEARCH = [
    ('БАК', 'Биохимический анализ крови'),
    ('ОАК', 'Общий анализ крови'),
    ('ОНК', 'Онкотест Pantum Detect'),
    ('ИНС', 'Инструментальная диагностика'),
    ('ЦИТ', 'Цитологические исследования'),
]


class Account(models.Model):
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    fathername = models.CharField(max_length=100, verbose_name='Отчество')
    age = models.IntegerField(verbose_name='Возраст')
    class Meta:
        abstract = True

class Doctors(Account):
    age = models.IntegerField(verbose_name='Возраст')
    specialization = models.CharField(max_length=100, verbose_name='Специализация', choices=SPECIALIZATION)
    experience = models.IntegerField(verbose_name='Стаж работы')
    def __str__(self):
        return str(self.surname)

# Create your models here.
class Clients(Account):
    phone = models.CharField(max_length=40, verbose_name='Телефон')
    email = models.CharField(max_length=100,verbose_name='Email', null= True, unique=True)
    city = models.CharField(max_length=100, verbose_name='Город')
    def __str__(self):
        return str(self.name)

class DoctorsSpecialization(models.Model):
    name = models.CharField(max_length=100, choices=SPECIALIZATION)
    doctor = models.ForeignKey("Doctors", on_delete=models.DO_NOTHING)  # продумать еще раз


class Consultation(models.Model):
    clients = models.ForeignKey('Clients', on_delete=models.CASCADE, null=True)
    doctors = models.ForeignKey('Doctors', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=False)


class Research(models.Model):
    name = models.CharField(max_length=20, choices=RESEARCH)
    description = models.CharField(max_length=255, null=True)
    def __str__(self):
        return str(self.name)

class Rating(models.Model):
    rating = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=255)
    class Meta:
        abstract = True


class DoctorsRating(Rating):
    doctor = models.ForeignKey('Doctors', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.doctor)


class ResearchesRating(Rating):
    research = models.ForeignKey('Research', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.research)
# создать класс Account для пользователя и доктора (абстрактный класс)
