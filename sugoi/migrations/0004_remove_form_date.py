# Generated by Django 3.2.3 on 2021-05-29 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sugoi', '0003_form_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='date',
        ),
    ]