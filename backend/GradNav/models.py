from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_male = models.BooleanField(default=True)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null = False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    product_image = models.FileField(upload_to='products') 
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        default='male',  # Set the default value to 'male'
    )

    def __str__(self):
        return self.name
    
class FemaleProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null = False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    product_image = models.FileField(upload_to='products') 

    def __str__(self):
        return self.name
    
class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
class FemaleBasket(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class BasketItem(models.Model):
    id = models.AutoField(primary_key=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def item_price(self):
        return self.product_id.price * self.quantity
    
    def __str__(self):
        return self.id
    
class FemaleBasketItem(models.Model):
    id = models.AutoField(primary_key=True)
    basket_id = models.ForeignKey(FemaleBasket, on_delete=models.CASCADE)
    product_id = models.ForeignKey(FemaleProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def item_price(self):
        return self.product_id.price * self.quantity
    
    def __str__(self):
        return self.id
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    shipping_addr = models.TextField(default="")

    def __str__(self):
        return self.customer_name
    
class FemaleOrder(models.Model):
    id = models.AutoField(primary_key=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    basket_id = models.ForeignKey(FemaleBasket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    shipping_addr = models.TextField(default="")

    def __str__(self):
        return self.customer_name
              
class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    details = models.TextField()
    satisfy = models.BooleanField()

    def __str__(self):
        return self.customer_name
    
class FemaleFeedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    product_id = models.ForeignKey(FemaleProduct, on_delete=models.CASCADE)
    details = models.TextField()
    satisfy = models.BooleanField()

    def __str__(self):
        return self.customer_name
    
    
