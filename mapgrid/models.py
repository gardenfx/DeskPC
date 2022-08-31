from django.db import models


class PC(models.Model):
    StatusChoice = [
        ('Свободен', 'Свободен'),
        ('Занят', 'Занят'),
        ('В обслуживании', 'В обслуживании'),
        ('Забронирован', 'Забронирован')
    ]
    ID_PC=models.AutoField('ID ПК', primary_key=True);
    Number = models.CharField('Номер ПК', max_length=3, null=True, unique=True);
    Status = models.CharField('Статус',max_length=20, choices=StatusChoice, default='Свободен');
    Stoim = models.DecimalField('Стоимость', max_digits=6, decimal_places=2, default=0);

    #def __unicode__(self):
    #    return self.ID_Klient

    def __str__(self):
        return self.Number

    def get_absolute_url(self):
        return '/map-grid/'

    class Meta:
        db_table='pc'
        verbose_name='ПК'
        verbose_name_plural='ПК'
