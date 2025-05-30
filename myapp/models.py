from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    address = models.TextField()
    password  = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_picture/')  
    usertype = models.CharField(max_length=100,default='buyer')

    def __str__(self):
        return self.fname + " "+self.lname 

class Product(models.Model):
    category = (
        ('men','men'),
        ('women','women'),
        ('kids','kids'),
    )

    size = (
        ('s','s'),
        ('m','m'),
        ('l','l'),
        ('xl','xl'),
        ('xxl','xxl'),
    )
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    product_category = models.CharField(max_length=100,choices=category)
    product_size = models.CharField(max_length=100,choices=size)
    product_name = models.CharField(max_length=100)
    product_price = models.PositiveBigIntegerField()
    product_picture = models.ImageField(upload_to='product_picture/')
    product_desc = models.TextField() 

    def __str__(self):
        return self.seller.fname + " - " + self.product_name  


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.fname + " " + self.product.product_name 
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_price = models.PositiveIntegerField()
    product_qty = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    payment_status = models.BooleanField(default=False)
    


    def __str__(self):
        return self.user.fname + " " + self.product.product_name 

