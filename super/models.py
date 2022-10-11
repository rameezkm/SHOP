from email.mime import image
from random import choices
from statistics import mode
from unicodedata import name
from urllib.parse import MAX_CACHE_SIZE
from django.db import models

GENDER=[
    ('male','male'),
    ('female','female'),
]
class Cool(models.Model):
    name=models.CharField(max_length=20)
    address=models.TextField(max_length=100)
    gender=models.TextField(choices=GENDER)
    phone=models.IntegerField(max_length=10)
    def __str__(self):
        return str(self.name)

class Hot(models.Model):
    product=models.CharField(max_length=20)
    prize=models.IntegerField(max_length=10)
    desc=models.TextField(max_length=10)
    image=models.CharField(max_length=200)
    def __str__(self):
        return str(self.product)