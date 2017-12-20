import hashlib

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Wheel, Nav, MustBuy, Shop, MainShow, FoodTypes, Goods, User


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


def urlToMarket(request):
    return redirect(reverse('axf:market', args=['104749', 0, 0]))


def cart(request):
    return render(request, 'axf/cart/cart.html')


def mine(request):
    # 配置基本信息
    title = '我的'

    usericon = ''
    username = request.session.get('username')
    if username == None:
        username = '未登录'
        is_login = False
    else:
        is_login = True
        user = User.objects.get(u_name=username)
        usericon = 'http://127.0.0.1:8000/static/uploadfiles/' + user.u_icon.url

    context = {
        'title': title,
        'username': username,
        'is_login': is_login,
        'usericon': usericon,
    }

    return render(request, 'axf/mine/mine.html', context)


def login(request):
    return render(request, 'axf/user/login.html')


def register(request):
    return render(request, 'axf/user/register.html')


def doRegister(request):
    try:
        # 存储用户信息
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        icon = request.FILES['icon']

        # 获取摘要
        md5 = hashlib.md5()
        # 将原数据传入进行摘要计算， 原数据需要转换成二进制
        md5.update(password.encode('utf-8'))
        # 获取摘要后的信息  hex 16进制   digest获取摘要输出
        # digest() 获取的是二进制的输出   hexdigest()  16进制的输出  可见字符串
        p = md5.hexdigest()
        password = p

        user = User()
        user.u_name = username
        user.u_password = password
        user.u_email = email
        user.u_phone = phone
        user.u_icon = icon

        user.save()

        # 存session
        request.session['username'] = username

    except Exception as e:
        # print(e)
        return HttpResponse('注册失败')

    return redirect(reverse('axf:mine'))


# 登出
def logout(request):
    del request.session['username']
    response = HttpResponseRedirect(reverse('axf:mine'))

    return response


def checkUser(request):
    uname = request.GET.get('uname')
    if User.objects.filter(u_name=uname):
        msg = '用户已存在'
        state = 201
    else:
        msg = '用户名可用'
        state = 200
    data = {'msg': msg, 'state': state}
    return JsonResponse(data)


'''
    使用摘要算法
        hashlib
        MD5
        sha
'''


def doLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    '''
        两种写法
            直接去数据库查询用户名和密码
            
            用用户名去查找，没找到提示用户
            用户名找到了再去验证密码
    '''
    user = User.objects.filter(u_name=username)
    if user:
        # 将密码进行两次hash算法后比较
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        newpassword = md5.hexdigest()
        if user[0].u_password == newpassword:
            request.session['username'] = username
            response = HttpResponseRedirect(reverse('axf:mine'))
            return response
        else:
            return redirect(reverse('axf:login'))
    else:
        return redirect(reverse('axf:login'))
