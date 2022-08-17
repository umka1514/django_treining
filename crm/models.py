from django.db import models


# Create your models here.

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Vaqt')
    order_name = models.CharField(max_length=200, verbose_name='Ism')
    order_phone = models.CharField(max_length=200, verbose_name='Telefon raqam')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Buyutma'
        verbose_name_plural = 'Buyutmalar'
