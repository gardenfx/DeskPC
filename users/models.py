from django.db import models


class Klient(models.Model):
    ID_Klient=models.AutoField(primary_key=True);
    Phone = models.CharField('Номер телефона',max_length=30, unique=True);
    Name = models.CharField('Имя', max_length=30);
    Data_rozjden = models.DateField('Дата рождения', );
    Skidka = models.CharField('Скидка', max_length=3, default=0);
    Balans = models.DecimalField('Баланс', max_digits= 10, decimal_places=2, default=0);

    def __unicode__(self):
        return self.ID_Klient

    def __str__(self):
        return self.Name

    def __str__(self):
        return self.Phone

    def get_absolute_url(self):
        return '/users/'

    class Meta:
        db_table='Klient'
        verbose_name='Клиент'
        verbose_name_plural='Клиенты'