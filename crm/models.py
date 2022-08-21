from django.db import models


# Create your models here.
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Status name')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Status name'
        verbose_name_plural = 'Status names'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Vaqt')
    order_name = models.CharField(max_length=200, verbose_name='Ism')
    order_phone = models.CharField(max_length=200, verbose_name='Telefon raqam')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Status')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Buyutma'
        verbose_name_plural = 'Buyutmalar'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Buyurtma')
    comment_text = models.TextField(verbose_name='Izoh')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Izoh yaratilgan sanasi')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'
