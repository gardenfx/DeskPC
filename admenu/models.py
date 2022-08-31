from django.db import models

class Admin(models.Model):
    ID_admin=models.AutoField(primary_key=True);
    FIO = models.CharField('ФИО', max_length=50, null=False);

    def __str__(self):
        return self.FIO

    def get_absolute_url(self):
        return '/admenu/'

    class Meta:
        db_table='admin'
        verbose_name='ФИО'
        verbose_name_plural='ФИО'
