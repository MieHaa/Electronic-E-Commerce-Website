from django.db import models
from django.contrib.auth.models import User
from item.models import Item
import uuid
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_set_cart')
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    
    
      
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.item.name
    
    @property
    def price(self):
        new_price = self.item.price * self.quantity
        return new_price
  
        
    
    