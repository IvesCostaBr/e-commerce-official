# Generated by Django 3.2.3 on 2021-05-19 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_carrinho_produtos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrinho',
            old_name='produtos',
            new_name='total_por_produto',
        ),
    ]
