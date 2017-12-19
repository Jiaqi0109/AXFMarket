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
