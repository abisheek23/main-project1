from django.db import models

# Create your models here.

class prodect(models.Model):
    pid=models.TextField()
    name=models.TextField()
    dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    stoct=models.IntegerField()
    img=models.FileField()