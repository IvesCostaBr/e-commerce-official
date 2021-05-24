# Generated by Django 3.2.3 on 2021-05-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_alter_carrinho_subtotal'),
        ('order', '0007_alter_order_all_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='all_produtos',
        ),
        migrations.AddField(
            model_name='order',
            name='all_produtos',
            field=models.ManyToManyField(blank=True, null=True, to='cart.ItemCarrinho'),
        ),
    ]
