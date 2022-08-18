from django.shortcuts import render
from .models import Order
from .forms import OrderForm

def first_page(request):
    order_lists = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'orders': order_lists, 'form': form})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    context = {
        'name': name,
        'phone': phone
    }

    print(isinstance(phone, int))
    s = Order(order_name=name, order_phone=phone)
    s.save()

    return render(request, './thanks_page.html', context)
