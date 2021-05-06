from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

def _str_(self):
    return self.name

def serialize(self):
    return f""" 
    <ProductDetails>
        <ProductId>{self.id}</PostId>
        <ProductName>{self.name}</PostName>
        <ProductDescription>{self.description}</PostDescription>
        <ProductPrice>{self.price}</PostPrice>
    </PostDetails>
    """ 

