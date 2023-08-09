FROM python:3.11

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR oncotest

CMD ["python","manage.py","runserver"]



# FROM python:3.11
#
# RUN mkdir Oncotest
#
# WORKDIR Oncotest
#
# COPY requirements.txt .
#
# RUN pip install -r requirements.txt
#
# COPY . .
# RUN cd oncotest

