from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
