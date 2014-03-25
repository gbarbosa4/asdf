from django.db import models

# Create your models here.

class Client(models.Model):
	name = models.TextField(max_length=100)
	city = models.TextField(max_length=100)
	address = models.TextField(max_length=100)
	telephone = models.IntegerField()
	dni = models.TextField(max_length=9)
	
class Car(models.Model):
	brand = models.TextField(max_length=30)
	model = models.TextField(max_length=30)
	price = models.IntegerField()
	car_id = models.IntegerField()

class Comercial(models.Model):
	company_id = models.TextField(max_length=100)
	name = models.TextField(max_length=100)
	city = models.TextField(max_length=100)
	address = models.TextField(max_length=100)
	telephone = models.IntegerField()
	dni = models.TextField(max_length=9)
	sells = models.IntegerField()

class Factory(models.Model):
	Factory_id = models.TextField(max_length=100)
	city = models.TextField(max_length=100)
	address = models.TextField(max_length=100)
	telephone = models.IntegerField()
	brand_car = models.TextField(max_length=30)
	production = models.IntegerField()
	stock = models.IntegerField()
	


