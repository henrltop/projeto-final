# Generated by Django 5.0.1 on 2024-03-13 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_automa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='numero',
            field=models.IntegerField(default=1),
        ),
    ]