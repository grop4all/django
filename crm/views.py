from django.shortcuts import render , get_object_or_404
from .models import Order

def main_page(request , order_id ):
    object_list = Order.objects.all()
    Title = 'main_page'
    return render(request, './index.html', {
        'object_list': object_list,
        'Title': Title
    })


def order_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    new_order = Order(order_name=name, order_phone=phone)
    new_order.save()
    return render(request, './order_page.html', {
        'new_order': new_order
    })
