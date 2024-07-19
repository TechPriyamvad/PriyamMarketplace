from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    created_by = models.ForeignKey(User,related_name="products",on_delete=models.CASCADE)
    def __str__(self):
        return self.name