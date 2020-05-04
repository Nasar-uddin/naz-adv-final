from django.db import models

# Create your models here.
class ContactText(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=200)
    subheading = models.TextField()
    def __str__(self):
        return self.heading

class Contacts(models.Model):
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)
    def __str__(self):
        return self.email
