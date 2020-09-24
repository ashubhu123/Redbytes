from django.db import models

# Create your models here.

user_title = (
   ('Customer','Customer'),
   ('Vendor','Vendor')
)

order_status =(
   ('Order Placed','Order Placed'),
   ('Order Accepted','Order Accepted'),
   ('Order Canceled','Order Canceled')
)

class UserRole(models.Model) :
   title = models.CharField(max_length=100,choices=user_title)
   is_active = models.BooleanField(default=False)

   def __str__(self):
      return self.title

class User(models.Model) :
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   email   = models.EmailField(unique=True)# (as username)
   password = models.CharField(max_length=120)
   is_active = models.BooleanField(default=False)
   role = models.ForeignKey(UserRole,on_delete=models.CASCADE)

   def __str__(self):
      return (f'{self.email}-{self.role}')

class Product(models.Model):
   product_name = models.CharField(max_length=120)
   price = models.FloatField(blank=True,null=True)

   def __str__(self):
      return (self.product_name)

class Order(models.Model):
   order_id = models.AutoField(primary_key=True)
   customer = models.ForeignKey(User,related_name='user_as_customer' ,on_delete=models.CASCADE) #(user with role customer)
   vendor = models.ForeignKey(User,related_name='user_as_vender',on_delete=models.CASCADE) # (user with role vendor)
   order_status = models.CharField(max_length=100,choices=order_status)

   def __str__(self):
      return str(self.order_id)

class OrderItem(models.Model):
   product = models.ForeignKey(Product,related_name='name_of_product',on_delete=models.CASCADE)
   quantity = models.IntegerField(default=0)
   price = models.FloatField()
   order = models.IntegerField()

   def __str__(self):
      return str(f'{self.id}-{self.product.product_name}')
