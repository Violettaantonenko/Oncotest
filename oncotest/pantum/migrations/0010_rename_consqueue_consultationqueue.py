# Generated by Django 4.2.2 on 2023-08-04 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pantum', '0009_consqueue_alter_clients_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConsQueue',
            new_name='ConsultationQueue',
        ),
    ]