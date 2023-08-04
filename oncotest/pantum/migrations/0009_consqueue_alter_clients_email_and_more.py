# Generated by Django 4.2.2 on 2023-07-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantum', '0008_consultation_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(verbose_name='значение')),
            ],
        ),
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='date',
            field=models.CharField(max_length=30, verbose_name='Дата'),
        ),
    ]