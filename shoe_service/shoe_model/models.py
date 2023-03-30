from django.db import models

# Create your models here.
class Shoe(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.IntegerField()
    availability = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.brand,
            "size": self.size,
            "availability": self.availability,
            "description": self.description,
            "price": self.price
        }
