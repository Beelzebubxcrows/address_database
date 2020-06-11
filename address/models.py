from django.db import models
from django.urls import reverse
# Create your models here.
class address(models.Model):
   
    hnumber= models.CharField(max_length = 30 ,blank = False)
    pincode = models.IntegerField(blank = False)
    locality = models.CharField( max_length = 30 ,blank = False)
    
    city = models.CharField( max_length = 30 ,blank = False)
    district = models.CharField( max_length = 30,blank = False)
    country = models.CharField(max_length = 30,blank = False)
    lattitude = models.CharField(max_length=30,blank=True)
    longitude= models.CharField(max_length=30,blank=True)
    

    def get_absolute_url(self):
         return reverse('success')