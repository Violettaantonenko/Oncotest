 Oncotest
 ======

 Описание
 --------
 Сайт с информацией об онкотестировании PanTum Detect, проводимых дополнительно исследованиях, врачах, которые ведут консультации.
 Посетитель сайта указав свое имя, электронную почту регистрируется. После регистрации он автоматически логинится. Есть личный кабинет, куда
 пациент вносит дополнительную информацию о себе.
 Изучив возможность проведения различных исследований пациент может оставить заявку на сайте, где указывает желаемое исследование, дату и номер телефона.
 После чего с ним связывается администратор для подтверждения записи.
 Пациент может оставить отзыв, заполнив форму на сайте.

 Реализация
 --------
 1.Install Python 3.11 interpreter:Addition information on https://www.python.org/downloads/
 2.Create and activate virtual environment for my project:py -m venv .venv_oncotest, .venv_oncotest\Scripts\activate
 3.Install requirements.txt
 4.Upload file gitignore 
 5.Install django: $pip install django(Django==4.2.2) 
 6.Start project:django-admin start project oncotest
 7. Create superuser: py manage.py createsuperuser
 8. Download my project to github: https://github.com/Violettaantonenko/Oncotest.git
 9. Create templates, models, forms, urls.
 10. Make migrattions
 11. Database: PostgreSQL
 
 Описание REST API:
 1. POST /api-auth/login/ -- логин
 2. пустой POST /api-auth/logout/ -- выход
 3. GET /api/ research/ -- все исследования
 4. POST /api/consultation/ -- создание консультации
 5. GET /api/doctors/1/ -- врач с id 1

