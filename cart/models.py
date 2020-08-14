from django.db      import models

from product.models import Product
from user.models    import User

class CartStatus(models.Model):
    status     = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cartstatus'

class Cart(models.Model):
    user       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product    = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cartstatus = models.ForeignKey(CartStatus, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'carts'

class Order(models.Model):
    user       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product    = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'
