from django.db import models

# Create your models here.
class ContactText(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=200)
    subheading = models.TextField()
    def __str__(self):
        return self.heading
