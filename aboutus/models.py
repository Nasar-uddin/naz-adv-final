from django.db import models

# Create your models here.
class AboutUsBanner(models.Model):
    heading = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.heading

class AboutUs(models.Model):
    heading = models.CharField(max_length=250)
    subheading = models.TextField()
    button = models.CharField(max_length=50)
    image_900x650 = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.heading

class Plan(models.Model):
    plan_number = models.IntegerField(default=1)
    heading = models.CharField(max_length=200)
    subheading = models.TextField()
    def __str__(self):
        return self.heading
class Mission(models.Model):
    heading = models.TextField(max_length=200)
    image_one_1000x700 = models.ImageField(upload_to="images/")
    image_two_500x730 = models.ImageField(upload_to="images/")
    subheading = models.TextField()
    our_approch_heading = models.CharField(max_length=200)
    our_approch_subheading = models.CharField(max_length=200)
    our_mission_heading = models.CharField(max_length=200)
    our_mission_subheading = models.CharField(max_length=200)
    def __str__(self):
        return self.heading