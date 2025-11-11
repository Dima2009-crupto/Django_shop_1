from django.db import models

# Create your models here.



class Product(models.Model):
    users = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"