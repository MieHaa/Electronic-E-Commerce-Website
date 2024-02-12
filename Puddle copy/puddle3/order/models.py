from django.db import models
from cart.models import Cart
from django.contrib.auth.models import User

# Create your models here.
# Show history of orders
# ▪ Sort by order date
# ▪ Sort by customer
# ▪ Sort by order size in dollar amount

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField()
    order_size = models.FloatField()
    
    def __str__(self):
        return f"{self.order_size} by {self.user.username}"