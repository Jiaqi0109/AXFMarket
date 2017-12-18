from django.shortcuts import render
from .models import Wheel


# Create your views here.
def home(request):
    # 查询主页面中的数据
    wheels = Wheel.objects.all()

    context = {'wheels': wheels}
    return render(request, 'axf/home/home.html', context)


def mine(request):
    return render(request, 'axf/mine/mine.html')


def market(request):
    return render(request, 'axf/market/market.html')


def cart(request):
    return render(request, 'axf/cart/cart.html')
