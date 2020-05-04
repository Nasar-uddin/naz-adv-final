from django.db import models

# Create your models here.
class PortfolioBanner(models.Model):
    heading = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.heading




