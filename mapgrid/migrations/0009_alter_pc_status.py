# Generated by Django 4.0.4 on 2022-05-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapgrid', '0008_alter_pc_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='Status',
            field=models.CharField(choices=[('Свободен', 'Свободен'), ('Занят', 'Занят'), ('В обслуживании', 'В обслуживании'), ('Забронирован', 'Забронирован')], default='Свободен', max_length=20, verbose_name='Статус'),
        ),
    ]