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


# Добавить класс для авторизации и аутентификацbb
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
    photo = models.ImageField(upload_to="photo_doctor", null=True, verbose_name='Фото')

    def __str__(self):
        return str(self.surname)

    class Meta:
        verbose_name = 'Врачи'
        verbose_name_plural = 'Врачи'


# Create your models here.
class Clients(Account):
    phone = models.CharField(max_length=40, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Email', null=True, unique=True)
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
    photo = models.ImageField(upload_to="photo_research", null=True, verbose_name='Фото')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Исследования'
        verbose_name_plural = 'Исследования'


class Reviews(models.Model):
    clients = models.ForeignKey('Clients', on_delete=models.CASCADE, null=True, verbose_name='Клиент')
    rating = models.PositiveIntegerField(null=True, verbose_name='Рейтинг')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return str(self.clients)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
