from django.db import models

# Create your models here.
class cource(models.Model):
    cid=models.TextField()
    cource_name=models.TextField()
    cource_dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()

class Message(models.Model):
    name=models.TextField()
    email=models.EmailField()
    message=models.TextField()