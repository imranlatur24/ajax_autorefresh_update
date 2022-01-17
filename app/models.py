from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobiles=models.BigIntegerField()
    class Meta:
        db_table="student"

class Listdata(models.Model):
    product_name = models.CharField(max_length=255,default='')
    class Meta:
        db_table="products"
    def __str__(self):
        return self.product_name