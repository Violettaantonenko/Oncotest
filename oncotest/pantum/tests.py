from django.test import TestCase
from .utils import Queue
import unittest
from django.test import Client
from .models import Research, Reviews,Consultation

class TestQueue(unittest.TestCase):
    def test_init_queue(self):
        queue = Queue('FIFO')

#проверяем, как добавляется значение и сравниваем число которое выводится с тем, которое добавили
    def test_add_and_return_fifo_value(self):
        queue = Queue("FIFO")
        first_value = 5
        queue.add(first_value)
        value = queue.pop()
        self.assertEqual(value,first_value)

    def test_add_and_return_fifo_multivalues(self):
        queue = Queue("FIFO")
        first_value = 5
        second_value = 1
        third_value = 1
        storage = [first_value, second_value, third_value]
        for val in storage:
            queue.add(val)
            value = queue.pop()
            self.assertEqual(value,val)
    def test_empty_queue(self):
        queue = Queue("FIFO")
        value = queue.pop()
        self.assertIs(value,None)



if __name__ == "__main__":
    unittest.main()

class TestPantumUrl(TestCase):
    def setUp(self):
        self.c = Client()

    def test_valid_research_url(self):
        self.response = self.c.get('/pantum/research/')
        self.assertEqual(self.response.status_code, 200)
        print(self.response.context['research'])

    def test_model_reviews(self):
        rating = 5
        description = 'good serves'
        self.reviews = Reviews.objects.create(rating=rating, description=description)
        self.assertEqual(self.reviews.rating, rating)
        self.assertEqual(self.reviews.description, description)
        # _meta возвращает экземпляр класса с заданным полем модели рейтин
        self.assertEqual(self.reviews._meta.get_field('rating').verbose_name, 'Рейтинг')
        self.assertEqual(self.reviews._meta.get_field('rating').blank, False)

    def test_model_consultation(self):
        service = 'УЗИ'
        date = '20.08.2023'
        phone = '+375295024707'
        self.consultation = Consultation.objects.create(service=service, date=date, phone=phone)
        self.assertEqual(self.consultation.service, service)
        self.assertEqual(self.consultation.date, date)
        self.assertEqual(self.consultation.phone, phone)
        self.assertEqual(self.consultation._meta.get_field('date').verbose_name, 'Дата')
        self.assertEqual(self.consultation._meta.get_field('service').blank, False)
