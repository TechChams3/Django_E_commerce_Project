from django.db import models
from django.conf import settings
# Create your models here.
from product.models import Product
from cart.models import Cupon
class OrderItem(models.Model):
    product = models.ForeignKey(Product,related_name='ordered',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return f"{self.product.title} x {self.quantity}"
    


class Order(models.Model):
    STATUS = ('Recieced','On the way','Delivered')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='orders',on_delete=models.CASCADE)
    order_item = models.ManyToManyField(OrderItem)
    coupon = models.ForeignKey(Cupon,null=True,blank=True,on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    address = models.TextField()
    total = models.DecimalField(max_digits=8,decimal_places=2)
    paid = models.BooleanField(default=True)
    transaction = models.UUIDField()
    status = models.CharField(max_length=15, choices=list(zip(STATUS,STATUS)))
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_date']


    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name



