# Generated by Django 5.0.1 on 2024-03-13 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_automa', '0003_remove_pedido_numero'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pedido',
            new_name='pedidos',
        ),
    ]
