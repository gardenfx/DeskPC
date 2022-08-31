from django.db import models
from admenu import admin
from users.models import Klient
from mapgrid.models import PC


class Kniga_ucheta(models.Model):
    ID_knig=models.AutoField(primary_key=True);
    Nomer_chek = models.IntegerField('Номер чека');
    Operac = models.CharField('Операция', max_length=45);
    Obsh_stoim = models.DecimalField('Общая стоимость', max_digits=6, decimal_places=2);
    Data_operac = models.DateTimeField('Дата операции');
    Admin_ID_admin = models.ForeignKey('admenu.Admin', on_delete=models.PROTECT, null=True, default=None, blank=True);
    Klient_ID_Klient = models.ForeignKey('users.Klient', on_delete=models.PROTECT, null=True, default = None, blank=True);
    Smen_ID_Smen = models.ForeignKey('Smen', on_delete=models.PROTECT, null=True, default=None);
    PC_ID_PC = models.ForeignKey('mapgrid.PC', on_delete=models.PROTECT, null=True, default=None);
    #def __unicode__(self):
    #    return self.ID_Klient

    def __unicode__ (self):
        return self.ID_knig

    def __unicode__(self):
        return self.Klient_ID_Klient

    def __unicode__(self):
        return self.Smen_ID_Smen

    def __unicode__(self):
        return self.PC_ID_PC

    def get_absolute_url(self):
        return '/rate/'

    class Meta:
        db_table='kniga_ucheta'
        verbose_name='Книгв учета'
        verbose_name_plural='Книга учета'

class Smen(models.Model):
    ID_Smen = models.AutoField('ID смены', primary_key=True);
    Data_smen = models.DateField('Дата смены')

    def __unicode(self):
        return self.ID_Smen

    class Meta:
        db_table='smen'
        verbose_name='Смена'
        verbose_name_plural='Смены'

