from django.db import models

SPECIALIZATION = [
    ('Гематолог', 'Врач-гематолог'),
    ('Онколог', 'Врач-онколог'),
    ('Терапев', 'Врач-терапевт'),
    ('Врач УЗД', 'Врач ультразвуковой диагностики'),
    ('Врач КДЛ', 'Врач клинико-лабораторной диагностики'),

]

RESEARCH = [
    ('Биохимический анализ крови', 'Биохимический анализ крови'),
    ('Общий анализ крови', 'Общий анализ крови'),
    ('Pantum Detect', 'Онкотест Pantum Detect'),
    ('Инструментальная диагностика', 'Инструментальная диагностика'),
    ('Цитологические исследования', 'Цитологические исследования'),
]

class Account(models.Model):
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    fathername = models.CharField(max_length=100, verbose_name='Отчество')
    age = models.IntegerField(verbose_name='Возраст')
    class Meta:
        abstract = True


class Doctors(Account):
    specialization = models.CharField(max_length=100, verbose_name='Специализация', choices=SPECIALIZATION)
    experience = models.IntegerField(verbose_name='Стаж работы')
    def __str__(self):
        return str(self.surname)

    class Meta:
        verbose_name = 'Врачи'
        verbose_name_plural = 'Врачи'

# Create your models here.
class Clients(Account):
    phone = models.CharField(max_length=40, verbose_name='Телефон')
    email = models.CharField(max_length=100,verbose_name='Email', null= True, unique=True)
    city = models.CharField(max_length=100, verbose_name='Город')
    def __str__(self):
        return str(self.surname)

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'

class DoctorsSpecialization(models.Model):
    name = models.CharField(max_length=100, choices=SPECIALIZATION, verbose_name='Специализация')
    doctor = models.ForeignKey("Doctors", on_delete=models.DO_NOTHING, verbose_name='Врач')  # продумать еще раз
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализация'

class Consultation(models.Model):
    clients = models.ForeignKey('Clients', on_delete=models.CASCADE, null=True, verbose_name='Клиент')
    doctors = models.ForeignKey('Doctors', on_delete=models.CASCADE, null=True, verbose_name='Врач')
    date = models.DateTimeField(auto_now=False, verbose_name='Дата')
    def __str__(self):
        return str(self.doctors)

    class Meta:
        verbose_name = 'Консультации'
        verbose_name_plural = 'Консультации'

class Research(models.Model):
    name = models.CharField(max_length=30, choices=RESEARCH, verbose_name='Исследование')
    description = models.CharField(max_length=1000, null=True, verbose_name='Описание')
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'Исследования'
        verbose_name_plural = 'Исследования'
class Rating(models.Model):
    rating = models.PositiveIntegerField(null=True, verbose_name='Рейтинг')
    description = models.CharField(max_length=255, verbose_name='Описание')
    class Meta:
        abstract = True


class DoctorsRating(Rating):
    doctor = models.ForeignKey('Doctors', on_delete=models.CASCADE, verbose_name='Врач')
    def __str__(self):
        return str(self.doctor)

    class Meta:
        verbose_name = 'Рейтинг врачей'
        verbose_name_plural = 'Рейтинг врачей'


class ResearchesRating(Rating):
    research = models.ForeignKey('Research', on_delete=models.CASCADE, verbose_name='Исследование')
    def __str__(self):
        return str(self.research)
    class Meta:
        verbose_name = 'Отзывы об исследовании'
        verbose_name_plural = 'Отзывы об исследовании'
# создать класс Account для пользователя и доктора (абстрактный класс)

