# Generated by Django 4.0.4 on 2022-06-01 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapgrid', '0009_alter_pc_status'),
        ('devices', '0007_alter_bron_komment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bron',
            name='PC_ID_PC',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mapgrid.pc'),
        ),
    ]