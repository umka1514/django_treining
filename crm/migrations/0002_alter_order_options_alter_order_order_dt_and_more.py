# Generated by Django 4.1 on 2022-08-21 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Buyutma', 'verbose_name_plural': 'Buyutmalar'},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_dt',
            field=models.DateTimeField(auto_now=True, verbose_name='Vaqt'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(max_length=200, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_phone',
            field=models.CharField(max_length=200, verbose_name='Telefon raqam'),
        ),
    ]
