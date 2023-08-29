from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering=('name',)
        verbose_name_plural ='Categories'
        
    def __str__(self):
        return self.name 
    
    
class Item(models.Model):
    category =models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null=True)
    price=models.FloatField() 
    image= models.ImageField(upload_to='item_images',blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    created_by =models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
          
          
    def __str__(self):
        return self.name
    
    
    
class Profile(models.Model):
    first_name=models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    age=models.IntegerField()
    prof_image=models.ImageField(upload_to='profile_images', blank=True, null=True)
    degree=models.CharField(max_length=500)
    email=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)
    product_selling=models.CharField(max_length=500)
    decription =models.TextField()
 
    
    
    def __str__(self):
        return self.first_name
    
        