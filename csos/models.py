from django.db import models
from django.conf import settings

# Create your models here.
class Cso(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)
    description = models.CharField(max_length=500,null=False, blank=True)
    date_published =models.DateTimeField(auto_now_add=True,verbose_name="date_updated")
    date_updated =models.DateTimeField(auto_now=True,verbose_name="date_updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
