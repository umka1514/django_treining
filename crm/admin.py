from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_name', 'order_phone', 'order_dt']
    ordering = ['order_name']


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
