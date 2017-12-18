from django.db import models


# Create your models here.

class Wheel(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_wheel'
