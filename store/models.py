

from django.db import models

class Product(models.Model):

    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name


