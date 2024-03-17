# Generated by Django 5.0.1 on 2024-03-15 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_automa', '0004_rename_pedido_pedidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_de_automação',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='pedidos',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_automa.tipo_de_automação'),
        ),
    ]
