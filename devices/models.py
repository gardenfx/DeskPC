from django.db import models
from mapgrid.models import PC

class Bron(models.Model):
    ID_Bron=models.AutoField(primary_key=True);
    Data_bron = models.DateTimeField('Дата и время брони');
    Phone_bron = models.CharField('Телефон', max_length=30);
    Name_bron = models.CharField('Имя', max_length=45);
    Komment = models.CharField('Комментарий', max_length=100, default=None, blank=True);
    PC_ID_PC = models.ForeignKey('mapgrid.PC', on_delete=models.PROTECT, null=True, default=None, blank=True)
    #def __unicode__(self):
    #    return self.ID_Klient

    def __str__(self):
        return self.Name_bron

    def get_absolute_url(self):
        return '/devices/'

    class Meta:
        db_table='bron'
        verbose_name='Бронирование'
        verbose_name_plural='Бронирование'
