from django.db import models
from users.models import Klient

class Oplat(models.Model):
    ID_Oplat=models.AutoField(primary_key=True);
    Data_opl = models.DateTimeField('Дата и время оплаты');
    Summ_opl = models.DecimalField('Сумма оплаты', max_digits=6, decimal_places=2);
    Klient_ID_Klient = models.ForeignKey('users.Klient', on_delete=models.PROTECT, null=True, default=None, blank=True)
    #def __unicode__(self):
    #    return self.ID_Klient

    def __unicode__(self):
        return self.ID_Oplat

    def get_absolute_url(self):
        return '/content/'

    class Meta:
        db_table='oplat'
        verbose_name='Оплата'
        verbose_name_plural='Оплаты'
