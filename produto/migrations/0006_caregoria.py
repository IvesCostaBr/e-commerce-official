# Generated by Django 3.2.3 on 2021-05-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_produto_image3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caregoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]