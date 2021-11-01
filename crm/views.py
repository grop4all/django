from django.shortcuts import render
from .models import Order


def main_page(request):
    object_list = Order.objects.all()
    Title = 'main_page'
    return render(request, './index.html', {
        'object_list': object_list,
        'Title': Title
    })
# Create your views here.
