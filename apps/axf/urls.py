from django.conf.urls import url

from apps.axf import views

urlpatterns = [
    url(r'^home/', views.home)
]
