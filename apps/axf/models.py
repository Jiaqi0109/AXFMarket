from django.db import models


# Create your models here.


# 首页轮播
class Wheel(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_wheel'


# 首页导航
class Nav(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_nav'


# 第二个轮播
class MustBuy(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_mustbuy'


# 便利商店
class Shop(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_shop'


# 主显示
class MainShow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=100)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=20)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=20)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_mainshow'


# 食品分类
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.CharField(max_length=100)

    class Meta:
        db_table = 'axf_foodtypes'


# 闪送
class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.BooleanField(default=False)
    pmdesc = models.IntegerField(default=0)
    specifics = models.CharField(max_length=20)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=50)
    dealerid = models.CharField(max_length=20)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


# 创建用户模型
class User(models.Model):
    '''
        用户名， 头像， 邮箱， 电话， 密码
    '''
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=50)
    u_icon = models.ImageField(upload_to='icons')
    u_email = models.CharField(max_length=50)
    u_phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_user'


class Order(models.Model):
    o_user = models.ForeignKey('User')
    o_status = models.IntegerField(default=0)


class Cart(models.Model):
    # 一条购物车对应一个用户， 一个用户可以对应多条购物车数据
    c_user = models.ForeignKey('User')
    # 一条购物车数据对应一个商品
    c_goods = models.ForeignKey('Goods')
    # 商品数量
    c_goods_num = models.IntegerField(default=1)
    #
    c_order = models.ForeignKey('Order', null=True, default=None)
    # 此数据是否选中
    c_selected = models.BooleanField(default=True)
    # 此数据属于购物车展示还是订单展示 false代表属于购物车， true代表属于订单
    c_belong = models.BooleanField(default=False)


