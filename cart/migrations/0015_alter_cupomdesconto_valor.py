# Generated by Django 3.2.3 on 2021-05-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_carrinho_cupom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupomdesconto',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]