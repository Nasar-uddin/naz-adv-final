from django.db import models

# Create your models here.


class Cover(models.Model):
  cover = models.ImageField(upload_to="images/")


class Service_Fields(models.Model):
  category = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  summary = models.TextField()

  def __str__(self):
      return self.title


class Service_Categories(models.Model):
  icon = models.ImageField(upload_to="images/")
  title = models.CharField(max_length=200)

  def __str__(self):
      return self.title


class Service_Tag(models.Model):
  tag = models.CharField(max_length=200)
  service_categories = models.ForeignKey(Service_Categories, on_delete=models.CASCADE)

  def __str__(self):
      return self.tag


class Why_Work(models.Model):
  image = models.ImageField(upload_to="images/")
  title = models.CharField(max_length=200)
  summary = models.TextField()

  def __str__(self):
      return self.title
