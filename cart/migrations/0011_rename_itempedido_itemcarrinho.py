# Generated by Django 3.2.3 on 2021-05-20 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
        ('cart', '0010_rename_total_por_produto_carrinho_produtos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemPedido',
            new_name='ItemCarrinho',
        ),
    ]
