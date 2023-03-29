from django.db import models

class Opinion(models.Model):
    fname = models.CharField(max_length=100),
    lname = models.CharField(max_length=100),
    email = models.CharField(max_length=100),
    product_id = models.CharField(max_length=50),
    product_name = models.CharField(max_length=100),
    content = models.CharField(max_length=500),
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '%s %s %s %s %s %s %s' % (self.fname, self.lname, self.email, self.product_id, self.product_name, self.content, self.created_at)

    def to_json(self):
        return {
            "First Name": self.fname,
            "Last Name": self.lname,
            "Username": self.email,
            "Product ID": self.product_id,
            "Product Name": self.product_name,
            "Create At": str(self.created_at)
        }