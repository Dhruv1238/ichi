# Generated by Django 3.2.3 on 2021-05-29 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugoi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='form',
            name='query',
            field=models.TextField(),
        ),
    ]
