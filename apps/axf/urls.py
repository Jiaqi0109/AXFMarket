from django.conf.urls import url

from apps.axf import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^mine/', views.mine, name='mine'),
    url(r'^market/$', views.urlToMarket, name='urlToMarket'),
    url(r'^market/(\d+)/(\d+)/(\d+)', views.market, name='market'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^login/', views.login, name='login'),
    url(r'^dologin/', views.doLogin, name='dologin'),
    url(r'^register/', views.register, name='register'),
    url(r'^doregister/', views.doRegister, name='doregister'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^checkuser/', views.checkUser, name='checkuser'),
    url(r'^addtocart/', views.addToCart, name='addtocart'),
    url(r'^changeselect/', views.changeSelect, name='changeselect'),
    url(r'^cartgoossub/', views.cartgoossub, name='cartgoossub'),
    url(r'^genorder/', views.genOrder, name='genorder'),
    url(r'^pay/(\d+)', views.pay, name='pay'),
]
