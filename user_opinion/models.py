from djongo import models

class Opinion(models.Model):
    fname = models.CharField( "fname",max_length=50)
    lname = models.CharField( "lname",max_length=50)
    email = models.CharField("email", max_length=50)
    product_id = models.CharField("product_id", max_length=50)
    product_name = models.CharField("product_name", max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    