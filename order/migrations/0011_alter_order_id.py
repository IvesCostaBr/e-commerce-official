# Generated by Django 3.2.3 on 2021-05-24 20:39

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_order_cod_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=order.models.generate_code, editable=False, primary_key=True, serialize=False),
        ),
    ]