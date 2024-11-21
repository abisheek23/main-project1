from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class prodect(models.Model):
    pid=models.TextField()
    name=models.TextField()
    dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    stoct=models.IntegerField()
    img=models.FileField()

class Cart(models.Model):
    product=models.ForeignKey(prodect,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField()
