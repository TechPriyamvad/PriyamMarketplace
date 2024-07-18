from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # to change table name inside admin dashboard
        verbose_name_plural = "Categories"
        # order records in ascending order
        ordering="name",
    
    # to show actual column values of a table instead of objects inside admin dashboard
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category,related_name="items",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name="items",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name