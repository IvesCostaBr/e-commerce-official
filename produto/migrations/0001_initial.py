# Generated by Django 3.2.3 on 2021-05-18 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('bio', models.CharField(blank=True, max_length=600, null=True)),
                ('image_protudo', models.FileField(blank=True, null=True, upload_to='produto<built-in function id>/')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
