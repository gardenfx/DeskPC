# Generated by Django 4.0.4 on 2022-05-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapgrid', '0002_alter_pc_status_alter_pc_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc',
            name='Number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Номер ПК'),
        ),
    ]