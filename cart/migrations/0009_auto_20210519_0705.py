# Generated by Django 3.2.3 on 2021-05-19 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
        ('cart', '0008_auto_20210519_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='total_por_produto',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='total_por_produto',
            field=models.ManyToManyField(blank=True, to='cart.ItemPedido'),
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='produto',
        ),
        migrations.AddField(
            model_name='itempedido',
            name='produto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='produto.produto'),
        ),
    ]
