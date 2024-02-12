from django.db import models
from cart.models import Cart

# Create your models here.
# Show history of orders
# ▪ Sort by order date
# ▪ Sort by customer
# ▪ Sort by order size in dollar amount

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="order")
    # quantity = models.IntegerField(default=0)
    order_date = models.DateTimeField()
    customer = models.CharField(max_length=50)
    order_size_in_dollars = models.FloatField()
    
    def __str__(self):
        return self.item.name
    
    @property
    def price(self):
        new_price = self.item.price * self.quantity
        return new_price