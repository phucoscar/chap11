from django.db import models

class Order(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    status = models.CharField(max_length=50)

    def to_json(self):
        return {
            "First Name": self.fname,
            "Last Name": self.lname,
            "Email": self.email,
            "Product ID": self.product_id,
            "Product Name": self.product_name,
            "Quantity": self.quantity,
            "Total Price": self.total_price,
            "Status": self.status
        }