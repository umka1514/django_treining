from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_name', 'order_phone', 'order_dt']
    ordering = ['order_name']


admin.site.register(Order, OrderAdmin)
