from django.db import models

# Create your models here.
class Frontend(models.Model):
    des = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    discount = models.CharField(max_length=10)
    price = models.IntegerField()
    # def __str__(self):
    #     return self.discount
