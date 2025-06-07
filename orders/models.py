from django.db import models
from products.models import VendorProducts
from accounts.models import Customer

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cart')
    is_paid = models.BooleanField(default=False)

    

    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(VendorProducts, null=True, on_delete=models.SET_NULL) 
    quantity = models.PositiveIntegerField(default=1)
    