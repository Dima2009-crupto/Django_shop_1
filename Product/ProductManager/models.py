from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()


def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"