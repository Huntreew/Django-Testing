from django.db import models

# Create your models here.


class Product(models.Model):
	title 	= models.CharField(max_length=100, null=True)
	price 	= models.DecimalField(max_digits=1000, decimal_places=2, null=True)
	summary = models.TextField(null=True)
 