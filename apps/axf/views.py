from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Wheel, Nav, MustBuy, Shop, MainShow, FoodTypes, Goods


# Create your views here.
def home(request):
    title = '首页'
    # 查询主页面中的数据
    wheels = Wheel.objects.all()
    # 查询导航数据
    navs = Nav.objects.all()
    # 查询必购数据, 第二个轮播
    mustbuys = MustBuy.objects.all()
    # 便利商店数据
    shops = Shop.objects.all()
    shops_more = shops[3:7]
    shops_rec = shops[7:11]
    # 查询mainshow
    mainshows = MainShow.objects.all()

    context = {
        'title': title,
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shops': shops,
        'shops_more': shops_more,
        'shops_rec': shops_rec,
        'mainshows': mainshows,
    }
    return render(request, 'axf/home/home.html', context)


def mine(request):
    return render(request, 'axf/mine/mine.html')


def market(request, typeid, childcid, sort_rule):
    title = '闪送超市'
    foodtypes = FoodTypes.objects.all()
    if childcid == '0':
        goods_list = Goods.objects.filter(categoryid=typeid)
    else:
        goods_list = Goods.objects.filter(categoryid=typeid).filter(childcid=childcid)

    # 排序
    if sort_rule == '1':
        goods_list = goods_list.order_by('productnum')
    elif sort_rule == '2':
        goods_list = goods_list.order_by('-productnum')
    elif sort_rule == '3':
        goods_list = goods_list.order_by('-price')
    elif sort_rule == '4':
        goods_list = goods_list.order_by('price')
    else:
        pass

    # 根据typeid把 childtypenames获取出来
    foodtype = FoodTypes.objects.filter(typeid=typeid)
    childtypenames = '全部分类:0'
    if foodtype:
        childtypenames = foodtype.first().childtypenames
    # 切割数据
    childtypenamelisttran = []
    childtypenamelist = childtypenames.split('#')
    for item in childtypenamelist:
        itemtran = item.split(':')
        childtypenamelisttran.append(itemtran)

    sort_rule_list = [['综合排序', '0'], ['销量升序', '1'], ['销量降序', '2'], ['价格最低', '3'], ['价格最高', '4']]

    context = {
        'foodtypes': foodtypes,
        'title': title,
        'goods_list': goods_list,
        'childtypenamelist': childtypenamelisttran,
        'typeid': typeid,
        'childcid': childcid,
        'sort_rule_list': sort_rule_list,
    }
    return render(request, 'axf/market/market.html', context)


def cart(request):
    return render(request, 'axf/cart/cart.html')


def urlToMarket(request):
    return redirect(reverse('axf:market', args=['104749', 0, 0]))
