# Generated by Django 4.0.4 on 2022-05-28 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='klient',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterField(
            model_name='klient',
            name='Phone',
            field=models.CharField(max_length=30, unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterModelTable(
            name='klient',
            table='Klient',
        ),
    ]