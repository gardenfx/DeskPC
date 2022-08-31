from django.db import models

class tovar(models.Model):
    ID_tovar=models.AutoField('ID товара', primary_key=True)
    Shtrih=models.CharField('Штрих-код', max_length=50, unique=True)
    Nazv_tovar=models.CharField('Название товара', max_length=50)
    Cen_tovar=models.DecimalField('Цена товара' ,max_digits=6, decimal_places=2, default=0)
    Vid_Tovar_ID_Vid=models.ForeignKey('vid_tovar', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return '/shop/'

    def __str__(self):
        return self.Nazv_tovar

    class Meta:
        db_table = 'tovar'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class vid_tovar(models.Model):
    ID_Vid = models.AutoField('ID товара', primary_key=True)
    Vid_Tov = models.CharField('Вид товара', max_length=50, unique=True)

    def __str__(self):
        return self.Vid_Tov

    def get_absolute_url(self):
        return '/shop/'

    class Meta:
        db_table = 'vid_tovar'
        verbose_name = 'Вид товара'
        verbose_name_plural = 'Виды товаров'
