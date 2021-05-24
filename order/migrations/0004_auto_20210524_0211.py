# Generated by Django 3.2.3 on 2021-05-24 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_alter_carrinho_subtotal'),
        ('order', '0003_order_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='produtos',
        ),
        migrations.AddField(
            model_name='order',
            name='all_produtos',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='cart.carrinho'),
            preserve_default=False,
        ),
    ]