from rate.models import Kniga_ucheta
import shop
import rate
from shop.models import tovar, vid_tovar
from django.db import models

class Opushen_tovar(models.Model):
    ID_Opushen_tovar = models.AutoField('ID отпущенных товаров', primary_key=True);
    Cen_opushen = models.DecimalField('Цена отпущенных товаров', max_digits=6, decimal_places=2);
    Kol = models.CharField('Количество', max_length=4, default=0);
    Tovar_ID_Tovar = models.ForeignKey(shop.models.tovar, on_delete=models.PROTECT, null=True);
    Kniga_ucheta_ID_knig = models.ForeignKey(rate.models.Kniga_ucheta, on_delete=models.PROTECT, null=True);

    def __unicode__(self):
        return self.ID_Opushen_tovar

    def get_absolute_url(self):
        return '/cashdesk/'

    class Meta:
        db_table = 'Opushen_tovar'
        verbose_name = 'Книга учета'
        verbose_name_plural = 'Книги учета'

