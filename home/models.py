from django.db import models

# Create your models here.
class Brand(models.Model):
  logo = models.ImageField(upload_to="images/")
  favicon = models.ImageField(upload_to="images/")

class Slider(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to="images/")

  def __str__(self):
      return self.title
  

class Service_Header(models.Model):
  title = models.CharField(max_length=200)
  summary = models.TextField()

  def __str__(self):
      return self.title


class Service_Body(models.Model):
  title = models.CharField(max_length=50)
  summary = models.TextField()
  icon = models.ImageField(upload_to="images/")

  def __str__(self):
      return self.title


class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Projects(models.Model):
  title = models.CharField(max_length=50)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  project_detail_heading = models.CharField(max_length=200, default="heading")
  project_detail_subheading = models.TextField(default="sub-heading")

  image = models.ImageField(upload_to="images/")

  def __str__(self):
      return self.title
      

class ProjectsImage(models.Model):
    projects = models.ForeignKey(Projects, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.projects.title

class ClientQuote(models.Model):
  quote = models.TextField()

  def __str__(self):
    return self.quote


class ClientBrand(models.Model):
  image = models.ImageField(upload_to="images/")


class Business(models.Model):
  title = models.CharField(max_length=50)
  summary = models.TextField()
  image = models.ImageField(upload_to="images/")

  def __str__(self):
      return self.title


class Technique(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to="images/")

  def __str__(self):
      return self.title


class Technique_Info(models.Model):
  title = models.CharField(max_length=200)
  summary = models.TextField()

  def __str__(self):
      return self.title
