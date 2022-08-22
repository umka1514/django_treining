from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram


def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    context = {
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'slider_list': slider_list,
        'form': OrderForm,
    }
    return render(request, './index.html', context=context)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        context = {
            'name': name,
        }
        s = Order(order_name=name, order_phone=phone)
        s.save()
        sendTelegram(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', context)
    else:
        return render(request, './thanks.html')
