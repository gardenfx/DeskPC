# Generated by Django 4.0.4 on 2022-05-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapgrid', '0004_alter_pc_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='Status',
            field=models.CharField(choices=[(1, 'Занят'), (2, 'Свободен'), (3, 'В обслуживании'), (4, 'Забронирован')], max_length=20, verbose_name='Статус'),
        ),
    ]
