from django.db import models

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    path = models.CharField(max_length=1000)

    def to_json(self):
        return {
            "Product ID": self.product_id,
            "Product Name": self.product_name,
            "Path": self.path
        }
