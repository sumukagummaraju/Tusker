from django.db import models

class Category(models.Model):
	cat_name = models.CharField(max_length=100)
	def __str__(self):
		return self.cat_name
class Subcat(models.Model):
	subcat_name = models.CharField(max_length=500)
	subcat_cat = models.ForeignKey(Category)
	def __str__(self):
		return self.subcat_name
class Products(models.Model):
	prod_width = models.CharField(max_length=5)
	prod_artno = models.CharField(max_length=50)
	prod_desc = models.CharField(max_length=500)
	prod_rps = models.FloatField(default=0)
	prod_stock = models.IntegerField(default=0)	
	prod_subcat = models.ForeignKey(Subcat)
	def __str__(self):
		return self.prod_artno
class Bill(models.Model):
	billnum = models.IntegerField(default = 0)