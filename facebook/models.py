from typing import Any
from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=100,null=True,blank=True,default='')
    last_name = models.CharField(max_length=100,null=True,blank=True,default='')
    email = models.CharField(max_length=100,null=True,blank=True,default='')
    password = models.CharField(max_length=255,null=True,blank=True,default='')
    mobile = models.BigIntegerField(default=0)
    gender = models.CharField(max_length=100,null=True,blank=True,default='')
    
    def __str__(self):
        return self.first_name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100,null=True, blank=True)
    category_image = models.ImageField(upload_to="upload/category")

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100,null=True, blank=True)
    product_image = models.ImageField(upload_to="upload/product")
    product_description = models.CharField(max_length=100,null=True, blank=True)
    product_price = models.IntegerField(default=0)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    address = models.CharField(max_length=200, blank=True)
    mobile = models.BigIntegerField(default=0)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Registration, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.first_name

