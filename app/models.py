from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import timezone to get current timeexit


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    special_instructions = models.TextField(default='No special instructions') 
    order_date = models.DateField(default=timezone.now)  


    def __str__(self):
        return f"Order {self.id} - {self.product.name}"

    # Custom save method to check if the user has already ordered the same product on the same day
    def save(self, *args, **kwargs):
        if Order.objects.filter(user=self.user, product=self.product, order_date=self.order_date).exists():
            raise ValueError("You have already ordered this product on this day.")
        super(Order, self).save(*args, **kwargs)

 



