from django.shortcuts import render, get_object_or_404
from home.models import Projects,ProjectsImage,Category,Brand
from .models import PortfolioBanner
# Create your views here.


def portfolio(request):
  brand = Brand.objects.all()[0]
  banner = PortfolioBanner.objects.all()[0]
  projects = Projects.objects.all()
  context = {
      'brand':brand,
      'banner':banner,
      'projects': projects,
     
  }
  return render(request, 'portfolio/portfolio.html', context)


def project_detail(request, category, id):
  brand = Brand.objects.all()[0]
  project = get_object_or_404(Projects, id=id)
  photos = ProjectsImage.objects.filter(projects=project)
  cat = get_object_or_404(Category, name=category)
  projects = Projects.objects.filter(category=cat.id)
  print(projects)
  context = {
      'brand':brand,
      'project': project,
      'photos': photos,
      'projects': projects
  }
  return render(request, 'portfolio/project_detail.html', context)
