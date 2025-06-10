from django.db import models
from django.contrib.auth.models import User

class Customer(User):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def getCartItemCount(self):
        from orders.models import CartItems
        return CartItems.objects.filter(cart__customer = self, cart__is_paid = False).count()


class Shopkeeper(User):
    gst_number = models.CharField(max_length=15)
    aadhar_number = models.CharField(max_length=12)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bmp_id = models.CharField(max_length=20, unique=True)
    vendor_name = models.CharField(max_length=100)
